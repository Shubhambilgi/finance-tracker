from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Read/update profile data. Password is never exposed."""

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'email', 'created_at', 'updated_at')


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Create a user from API input. Password is write-only and hashed via create_user."""

    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        style={'input_type': 'password'},
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            'password_confirm',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        email = User.objects.normalize_email(value)
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError('A user with this email already exists.')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError(
                {'password_confirm': 'Passwords do not match.'}
            )

        validate_password(password)
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        email = validated_data.pop('email')

        # AbstractUser still has a unique username field; store email there
        # so registration works until USERNAME_FIELD is fully switched to email.
        return User.objects.create_user(
            email=email,
            password=password,
            username=email,
            **validated_data,
        )


class UserLoginSerializer(serializers.Serializer):
    """Validate email + password. Does not create tokens (that is Day 5 / JWT)."""

    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
    )

    def validate(self, attrs):
        email = User.objects.normalize_email(attrs.get('email', ''))
        password = attrs.get('password')

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid email or password.')

        if not user.is_active:
            raise serializers.ValidationError('This account is inactive.')

        attrs['user'] = user
        attrs['email'] = user.email
        return attrs
