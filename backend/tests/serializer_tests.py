"""One-off Day 3 serializer checks. Run: python _day3_serializer_tests.py"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import transaction as db_transaction

from users.models import User
from users.serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserSerializer,
)
from transactions.serializers import BudgetSerializer, TransactionSerializer

print('=' * 60)
print('DAY 3: API SERIALIZER TESTS')
print('=' * 60)

sideline = db_transaction.atomic()
sideline.__enter__()

try:
    print('\n[1] UserRegistrationSerializer — valid payload')
    reg_data = {
        'email': 'day3-serializer@example.com',
        'first_name': 'Shubham',
        'last_name': 'Bilgi',
        'password': 'StrongPass123!',
        'password_confirm': 'StrongPass123!',
    }
    reg = UserRegistrationSerializer(data=reg_data)
    assert reg.is_valid(), reg.errors
    user = reg.save()
    print('  created id=', user.id, 'email=', user.email)
    print('  password hashed=', user.password != 'StrongPass123!')
    print('  JSON =', UserSerializer(user).data)

    print('\n[2] UserRegistrationSerializer — password mismatch (expect fail)')
    bad_reg = UserRegistrationSerializer(data={
        **reg_data,
        'email': 'mismatch@example.com',
        'password_confirm': 'DifferentPass123!',
    })
    print('  is_valid=', bad_reg.is_valid(), 'errors=', dict(bad_reg.errors))

    print('\n[3] UserRegistrationSerializer — duplicate email (expect fail)')
    dup = UserRegistrationSerializer(data=reg_data)
    print('  is_valid=', dup.is_valid(), 'errors=', dict(dup.errors))

    print('\n[4] UserLoginSerializer — correct credentials')
    login = UserLoginSerializer(data={
        'email': 'day3-serializer@example.com',
        'password': 'StrongPass123!',
    })
    assert login.is_valid(), login.errors
    print('  authenticated user=', login.validated_data['user'].email)

    print('\n[5] UserLoginSerializer — wrong password (expect fail)')
    bad_login = UserLoginSerializer(data={
        'email': 'day3-serializer@example.com',
        'password': 'wrong-password',
    })
    print('  is_valid=', bad_login.is_valid(), 'errors=', bad_login.errors)

    print('\n[6] TransactionSerializer — income + expense')
    tx_income = TransactionSerializer(data={
        'user': user.id,
        'amount': '2500.00',
        'category': 'salary',
        'description': 'September paycheck',
        'type': 'income',
        'date': '2026-09-01',
    })
    assert tx_income.is_valid(), tx_income.errors
    income = tx_income.save()
    print('  income JSON =', TransactionSerializer(income).data)

    tx_expense = TransactionSerializer(data={
        'user': user.id,
        'amount': '50.99',
        'category': 'groceries',
        'description': 'Weekly shop',
        'type': 'expense',
        'date': '2026-09-13',
    })
    assert tx_expense.is_valid(), tx_expense.errors
    expense = tx_expense.save()
    print('  expense JSON =', TransactionSerializer(expense).data)

    print('\n[7] TransactionSerializer — amount <= 0 (expect fail)')
    bad_tx = TransactionSerializer(data={
        'user': user.id,
        'amount': '0.00',
        'category': 'groceries',
        'type': 'expense',
        'date': '2026-09-13',
    })
    print('  is_valid=', bad_tx.is_valid(), 'errors=', dict(bad_tx.errors))

    print('\n[8] TransactionSerializer — invalid type (expect fail)')
    bad_type = TransactionSerializer(data={
        'user': user.id,
        'amount': '10.00',
        'category': 'other',
        'type': 'transfer',
        'date': '2026-09-13',
    })
    print('  is_valid=', bad_type.is_valid(), 'errors=', dict(bad_type.errors))

    print('\n[9] BudgetSerializer — valid budget')
    budget_ser = BudgetSerializer(data={
        'user': user.id,
        'category': 'groceries',
        'limit': '300.00',
        'month': '2026-09-01',
    })
    assert budget_ser.is_valid(), budget_ser.errors
    budget = budget_ser.save()
    print('  budget JSON =', BudgetSerializer(budget).data)

    print('\n[10] BudgetSerializer — duplicate user/category/month (expect fail)')
    dup_budget = BudgetSerializer(data={
        'user': user.id,
        'category': 'groceries',
        'limit': '400.00',
        'month': '2026-09-01',
    })
    print('  is_valid=', dup_budget.is_valid(), 'errors=', dup_budget.errors)

    print('\n[11] BudgetSerializer — limit <= 0 (expect fail)')
    bad_limit = BudgetSerializer(data={
        'user': user.id,
        'category': 'entertainment',
        'limit': '-10.00',
        'month': '2026-09-01',
    })
    print('  is_valid=', bad_limit.is_valid(), 'errors=', dict(bad_limit.errors))

    print('\n' + '=' * 60)
    print('ALL SERIALIZER CHECKS COMPLETED')
    print('=' * 60)
finally:
    db_transaction.set_rollback(True)
    sideline.__exit__(None, None, None)
    print('\nRolled back test data (no leftover rows).')
