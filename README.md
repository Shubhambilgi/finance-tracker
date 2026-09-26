# Personal Finance Tracker

A full-stack personal finance application designed to help users track income, expenses, budgets, and spending patterns. The project combines a Django backend with a future-ready frontend architecture focused on practical financial management and data visibility.

## Project Summary

This application is built to support:

- personal transaction tracking
- category-based budgeting
- income and expense classification
- financial insight generation
- a scalable foundation for future analytics and dashboard features

## Tech Stack

- Backend: Django + Django REST Framework
- Database: SQLite for local development
- Authentication: custom email-based user model
- API Layer: serializers and REST-ready structure for users, transactions, and budgets
- Planned Frontend: React + TypeScript + Tailwind CSS

## Key Features

- secure, email-based user authentication model
- transaction management for income and expense entries
- budget support for monthly category limits
- validation for business rules at the serializer layer
- structured backend foundation for future API and dashboard work

## Architecture

```text
finance-tracker/
├── backend/
│   ├── config/
│   ├── users/
│   ├── transactions/
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
├── docs/
├── LICENSE
├── README.md
└── .gitignore
```

## Getting Started

### Backend Setup

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The backend runs locally at:

- http://127.0.0.1:8000/

### Create an Admin User

```bash
python manage.py createsuperuser
```

## Core Data Models

### User
- unique email-based identity
- hashed password storage
- first name and last name
- created/updated timestamps

### Transaction
- linked user
- amount
- category
- description
- type: income or expense
- date
- created timestamp

### Budget
- linked user
- category
- monthly spending limit
- month reference
- updated timestamp

## Roadmap

Planned enhancements include:

- REST API endpoints for users, transactions, and budgets
- JWT-based authentication
- dashboard summaries and spending analytics
- category-wise visualization and reporting
- frontend interface for finance management

## Documentation

Project notes and development documentation are stored in the docs directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

- GitHub: [github.com/Shubhambilgi](https://github.com/Shubhambilgi)
- LinkedIn: www.linkedin.com/in/shubham-bilgi-234044283
- Email: shubhambilgi@gmail.com
