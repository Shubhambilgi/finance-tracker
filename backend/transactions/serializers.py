from decimal import Decimal

from rest_framework import serializers

from users.models import User

from .models import TRANSACTION_TYPES, Budget, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """Turn Transaction rows into JSON and validate create/update input."""

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'amount',
            'category',
            'description',
            'type',
            'date',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')

    def validate_amount(self, value):
        if value <= Decimal('0'):
            raise serializers.ValidationError('Amount must be greater than 0.')
        return value

    def validate_category(self, value):
        category = value.strip()
        if not category:
            raise serializers.ValidationError('Category cannot be empty.')
        return category

    def validate_type(self, value):
        allowed = {choice[0] for choice in TRANSACTION_TYPES}
        if value not in allowed:
            raise serializers.ValidationError(
                f'Type must be one of: {", ".join(sorted(allowed))}.'
            )
        return value


class BudgetSerializer(serializers.ModelSerializer):
    """Turn Budget rows into JSON and enforce one budget per user/category/month."""

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Budget
        fields = (
            'id',
            'user',
            'category',
            'limit',
            'month',
            'updated_at',
        )
        read_only_fields = ('id', 'updated_at')

    def validate_limit(self, value):
        if value <= Decimal('0'):
            raise serializers.ValidationError('Budget limit must be greater than 0.')
        return value

    def validate_category(self, value):
        category = value.strip()
        if not category:
            raise serializers.ValidationError('Category cannot be empty.')
        return category

    def validate(self, attrs):
        user = attrs.get('user') or getattr(self.instance, 'user', None)
        category = attrs.get('category') or getattr(self.instance, 'category', None)
        month = attrs.get('month') or getattr(self.instance, 'month', None)

        queryset = Budget.objects.filter(user=user, category=category, month=month)
        if self.instance is not None:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                'A budget already exists for this user, category, and month.'
            )

        return attrs
