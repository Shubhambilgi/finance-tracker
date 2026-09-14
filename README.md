💰 Personal Finance Tracker

A full-stack web application for managing personal finances with transaction tracking, budget management, and data visualization.

Status: 🚀 In Development

🎯 What This Project Does

Track your income and expenses, set monthly budgets, and visualize your spending patterns with beautiful charts.

🛠️ Tech Stack

Backend: Django 6.1 + Django REST Framework + PostgreSQL
Frontend: React 18 + TypeScript + Tailwind CSS + Recharts
Authentication: JWT (Email-based)

📁 Project Structure
finance-tracker/
├── backend/
│   ├── venv/                     # Virtual environment
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── users/
│   │   ├── models.py             # Custom User model
│   │   ├── admin.py
│   │   ├── serializers.py        # (coming)
│   │   └── views.py              # (coming)
│   ├── transactions/
│   │   ├── models.py             # Transaction & Budget
│   │   ├── admin.py
│   │   ├── serializers.py        # (coming)
│   │   └── views.py              # (coming)
│   └── manage.py
├── frontend/                     # (coming)
├── docs/                         # Progress & documentation
│   ├── Day1-UserModel.md
│   ├── Day2-TransactionBudgetModels.md
│   └── screenshots/
└── README.md
🚀 Quick Start
Backend Setup
bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt python-dotenv

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver

Backend: http://localhost:8000
Admin: http://localhost:8000/admin

✨ Features
✅ Custom User model (email-based authentication)
✅ Transaction model (income & expense tracking)
✅ Budget model (monthly spending limits)
⏳ REST API endpoints
⏳ React frontend
⏳ Data visualization (charts)
⏳ Dashboard
📊 Database Models
User
- email (unique)
- password (hashed)
- first_name
- last_name
- created_at
- updated_at
Transaction
- user (ForeignKey)
- amount (DecimalField)
- category (CharField)
- description (TextField, optional)
- type (choice: income/expense)
- date (DateField)
- created_at
Budget
- user (ForeignKey)
- category (CharField)
- limit (DecimalField)
- month (DateField)
- updated_at
- unique_together: (user, category, month)
🧪 Testing
Test User Creation
bash
python manage.py shell

>>> from users.models import User
>>> user = User.objects.create_user(
...     email='test@example.com',
...     password='testpass123',
...     first_name='Test',
...     last_name='User'
... )
>>> print(user.email)
test@example.com
Test Transaction & Budget
bash
python manage.py shell

>>> from users.models import User
>>> from transactions.models import Transaction, Budget
>>> from datetime import date

>>> user = User.objects.first()

>>> transaction = Transaction.objects.create(
...     user=user,
...     amount=50.99,
...     category='groceries',
...     type='expense',
...     date=date.today()
... )
>>> print(transaction)
groceries - $50.99 (2026-09-13)

>>> budget = Budget.objects.create(
...     user=user,
...     category='groceries',
...     limit=300.00,
...     month=date(2026, 9, 1)
... )
>>> print(budget)
groceries - $300.00 (2026-09-01)
Admin Panel
Go to http://127.0.0.1:8000/admin
Login with superuser credentials
Browse Users, Transactions, Budgets sections
🔐 Authentication

Uses JWT (JSON Web Tokens) with email-based login.

Why custom User model?

✅ Email instead of username (modern approach)
✅ Industry best practice
✅ More flexible for future features
✅ Better security control
📚 Documentation

See /docs/ folder for detailed daily progress and learnings:

Daily development notes
Code explanations
Screenshots
Troubleshooting
🐛 Troubleshooting
Virtual Environment Not Activated
bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Database Issues
bash
# Reset database
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
Port Already in Use
bash
python manage.py runserver 8001
📝 Git Workflow
bash
# Create feature branch
git checkout -b feature/feature-name

# Make changes
git add .
git commit -m "feat: add new feature"

# Push
git push origin feature/feature-name
📞 Contact
GitHub: github.com/Shubhambilgi
LinkedIn: linkedin.com/in/shubham-bilgi
Email: shubhambilgi@gmail.com
📄 License

MIT License - see LICENSE file for details.

🚀 Getting Involved

This is a learning project. Follow the /docs/ folder for daily progress and updates.

<div align="center">

Built by: Shubham Bilgi

Made with ❤️ for learning

</div>