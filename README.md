# 💰 Personal Finance Tracker

A full-stack web application for managing personal finances with transaction tracking, budget management, and data visualization. Built with Django REST Framework and React.

**Status:** 🚀 In Development

---

## 🎯 Project Overview

**Personal Finance Tracker** is a modern web application that helps users manage their finances efficiently. Track income and expenses, set budgets, visualize spending patterns, and gain insights into your financial habits.

### Why This Project?

This project demonstrates:
- ✅ Full-stack development capabilities (backend + frontend)
- ✅ REST API design and implementation
- ✅ Database architecture and optimization
- ✅ Authentication and authorization
- ✅ Real-time data visualization
- ✅ Professional Git workflow and documentation

---

## ✨ Features

### Core Features (Planned)

- **User Authentication**
  - Email-based signup and login
  - JWT token authentication
  - Secure password hashing

- **Transaction Management**
  - Add, edit, delete transactions
  - Track income and expenses
  - Categorize transactions
  - Search and filter capabilities

- **Budget Tracking**
  - Set monthly budgets by category
  - Track spending vs budget
  - Receive alerts when near limit
  - Historical budget analysis

- **Data Visualization**
  - Monthly spending charts
  - Category breakdown pie charts
  - Trend analysis
  - Income vs expense comparison

- **Dashboard**
  - Balance overview
  - Recent transactions
  - Budget status
  - Quick statistics

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 6.1 + Django REST Framework
- **Database:** SQLite (development) → PostgreSQL (production)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **API:** RESTful API design
- **Language:** Python 3.13

### Frontend
- **Framework:** React 18
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **State Management:** Zustand
- **Charts:** Recharts
- **HTTP Client:** Axios
- **Routing:** React Router

### DevOps & Tools
- **Version Control:** Git & GitHub
- **Deployment:** Render / Railway (planned)
- **Package Manager:** pip (backend), npm (frontend)
- **Virtual Environment:** venv

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.8 or higher
  ```bash
  python --version
  ```

- **Node.js** 14 or higher (for frontend)
  ```bash
  node --version
  ```

- **Git**
  ```bash
  git --version
  ```

- **Git account** (for cloning)

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
cd finance-tracker
```

### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt python-dotenv

# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

**Backend will run at:** `http://localhost:8000`

### 3. Frontend Setup (Coming Soon)

```bash
# Navigate back to root, then frontend
cd ../frontend

# Install dependencies
npm install

# Start development server
npm run dev

---

## 📁 Project Structure

```
finance-tracker/
│
├── backend/
│   ├── venv/                          # Virtual environment
│   ├── config/
│   │   ├── settings.py               # Django settings
│   │   ├── urls.py                   # URL routing
│   │   └── wsgi.py                   # WSGI config
│   ├── users/
│   │   ├── models.py                 # Custom User model
│   │   ├── serializers.py            # DRF serializers (coming)
│   │   ├── views.py                  # API views (coming)
│   │   ├── admin.py                  # Admin configuration
│   │   └── migrations/
│   ├── transactions/
│   │   ├── models.py                 # Transaction & Budget models (coming)
│   │   ├── serializers.py            # Serializers (coming)
│   │   ├── views.py                  # API views (coming)
│   │   └── migrations/
│   ├── manage.py                     # Django management
│   ├── db.sqlite3                    # Database (development)
│   └── requirements.txt              # Python dependencies
│
├── frontend/                         # (Coming in Week 2)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
│
├── docs/                            # Documentation
│   ├── Day1-UserModel.md           # Daily learnings
│   ├── Day2-TransactionModel.md    # (Coming)
│   ├── screenshots/
│   │   ├── Day1-admin-panel.png
│   │   └── Day1-shell-user-test.png
│   └── learning-notes.md
│
├── README.md                        # This file
├── .gitignore                       # Git ignore rules
├── LICENSE                          # MIT License
└── CONTRIBUTING.md                  # (Coming)
```

---

## 🎯 Current Status (Day 1)

### ✅ Completed

- [x] GitHub repository setup
- [x] Django project structure
- [x] Custom User model with email authentication
- [x] CustomUserManager for email-based login
- [x] Database migrations
- [x] Django admin configuration
- [x] User testing in Django shell
- [x] Admin panel setup

### ⏳ In Progress

- [ ] Transaction model
- [ ] Budget model
- [ ] API serializers
- [ ] REST API endpoints
- [ ] Postman testing
- [ ] React frontend setup
- [ ] Frontend integration

### 📅 Planned

- [ ] Charts and data visualization
- [ ] User authentication on frontend
- [ ] Dashboard UI
- [ ] Testing suite
- [ ] Deployment setup
- [ ] Documentation completion

---

## 📚 Daily Progress

Track the daily development progress and learnings:

- **[Day 1: Custom User Model](docs/Day1-UserModel.md)** ✅
  - Custom User model with email authentication
  - CustomUserManager implementation
  - Admin panel setup
  - Database migrations

- **[Day 2: Transaction Model](docs/Day2-TransactionModel.md)** ⏳
  - Transaction and Budget models
  - Database relationships
  - API serializers

---

## 🔐 Authentication

### Current Implementation

The project uses **JWT (JSON Web Tokens)** for authentication:

```
User Registration → Email + Password → JWT Token → Authenticated Requests
```

### Custom User Model

Why a custom User model?

- ✅ Uses **email** instead of username for login (modern approach)
- ✅ Industry best practice (recommended by Django)
- ✅ Flexible for future customizations
- ✅ Better security control

### CustomUserManager

Handles user creation without requiring username:

```python
user = User.objects.create_user(
    email='user@example.com',
    password='secure_password',
    first_name='John',
    last_name='Doe'
)
```

---

## 📊 Database Schema

### User Model

```
User
├── id (UUID)
├── email (unique)
├── password (hashed)
├── first_name
├── last_name
├── is_active
├── is_staff
├── created_at (auto-set)
└── updated_at (auto-update)
```

### Transaction Model (Coming Soon)

```
Transaction
├── id
├── user_id (FK)
├── amount
├── category
├── description
├── type (income/expense)
├── date
└── created_at
```

### Budget Model (Coming Soon)

```
Budget
├── id
├── user_id (FK)
├── category
├── limit
├── month
└── updated_at
```

---

## 🧪 Testing

### Manual Testing (Current)

Test User creation in Django shell:

```bash
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
```

### Admin Panel Testing

1. Start server: `python manage.py runserver`
2. Go to: `http://127.0.0.1:8000/admin`
3. Login with superuser credentials
4. View Users section

### Automated Testing (Coming)

- Django TestCase for models
- DRF APITestCase for endpoints
- Frontend Jest tests

---

## 📸 Screenshots

### Admin Panel
![Admin Panel](docs/screenshots/Day1-admin-panel.png)
*Django admin panel showing custom User model*

### Shell Testing
![Shell Test](docs/screenshots/Day1-shell-user-test.png)
*User creation and testing in Django shell*

---

## 🚀 Deployment (Planned)

### Backend Deployment
- **Platform:** Render or Railway
- **Database:** PostgreSQL
- **Server:** Gunicorn

### Frontend Deployment
- **Platform:** Vercel or Netlify
- **Build:** npm run build

### Environment Variables

```env
# Backend (.env)
DEBUG=False
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@host/db
CORS_ALLOWED_ORIGINS=https://your-frontend.com

# Frontend (.env)
VITE_API_URL=https://your-backend.com/api
```

---

## 🤝 Contributing

This is a personal learning project, but contributions and feedback are welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) (coming soon) for guidelines.

---

## 📖 Learning Resources

### Used In This Project

- [Django Official Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Custom User Model](https://docs.djangoproject.com/en/6.1/topics/auth/customizing/)
- [React Documentation](https://react.dev/)

### Recommended Learning

- Real Python Django Tutorials
- Full Stack Python
- MDN Web Docs

---

## 🎓 What I'm Learning

### Backend
- ✅ Django ORM and models
- ✅ Custom authentication
- ✅ REST API design
- ⏳ Query optimization
- ⏳ Testing strategies
- ⏳ Deployment

### Frontend
- ⏳ React hooks and state management
- ⏳ API integration
- ⏳ Data visualization
- ⏳ Form handling
- ⏳ Responsive design

### DevOps
- ⏳ Docker & Docker Compose
- ⏳ CI/CD pipelines
- ⏳ Production deployment
- ⏳ Database optimization

---

## 🐛 Troubleshooting

### Virtual Environment Issues

**Problem:** `ModuleNotFoundError: No module named 'django'`

**Solution:** Activate virtual environment
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Database Issues

**Problem:** `InconsistentMigrationHistory`

**Solution:** Reset database
```bash
del db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

### Port Already in Use

**Problem:** `Address already in use`

**Solution:** Use different port
```bash
python manage.py runserver 8001
```

---

## 📝 Development Notes

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/user-auth

# Make changes and commit
git add .
git commit -m "feat: implement custom user model"

# Push to GitHub
git push origin feature/user-auth

# Create Pull Request on GitHub
```

### Code Standards

- Follow PEP 8 for Python
- Use meaningful variable names
- Write docstrings for classes and functions
- Keep functions small and focused

---

## 📞 Contact & Support

- **GitHub:** [github.com/Shubhambilgi](https://github.com/Shubhambilgi/)
- **LinkedIn:** [linkedin.com/in/shubham-bilgi](https://www.linkedin.com/in/shubham-bilgi-234044283/)
- **Email:** shubhambilgi@gmail.com

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 🎉 Project Timeline

| Timeline | Status | Details |
|----------|--------|---------|
| **Week 1** | 🚀 In Progress | Backend setup, User model, API foundation |
| **Week 2** | ⏳ Coming | Frontend setup, Integration, Charts |
| **Week 3** | ⏳ Coming | Testing, Bug fixes, Polish |
| **Week 4** | ⏳ Coming | Deployment, Documentation, Final polish |

---

## 🌟 Highlights

### Why This Project Stands Out

1. **Daily Documentation** 📚
   - Each day has dedicated README with learnings
   - Code explanations and concepts
   - Screenshots and progress tracking

2. **Professional Practices** 🏆
   - Clean git history with meaningful commits
   - Proper folder structure
   - Environment configuration
   - Error handling and troubleshooting

3. **Learning Focused** 🎓
   - Not just code, but understanding
   - Explanations of WHY decisions were made
   - Links to resources and documentation
   - Common pitfalls and solutions

4. **Portfolio Ready** 💼
   - Comprehensive README (this file!)
   - Screenshots of working features
   - Clear project structure
   - Deployment instructions

---

## 🎯 Next Steps

1. **In Progress:** Build Transaction and Budget models
2. **Week 1:** Complete REST API endpoints
3. **Week 2:** Build React frontend
4. **Week 3:** Integrate frontend with backend
5. **Week 4:** Deploy and finalize

---

## 📊 Project Stats

- **Started:** September 12, 2026
- **Daily Commits:** Planned ✅
- **Documentation:** Comprehensive 📚
- **Code Quality:** Professional 💪
- **Learning Focus:** Deep 🧠

---

## ✅ Checklist for Success

- [x] GitHub repo setup
- [x] Project structure
- [x] Custom User model
- [ ] REST API complete
- [ ] Frontend complete
- [ ] Deployment ready
- [ ] Full documentation
- [ ] Test coverage

---

## 🚀 Ready to Build?

This project is a journey from zero to production. Each day builds upon the previous, creating a complete, deployable application.

**Follow the daily progress in the [docs/](docs/) folder!**

---

<div align="center">

### 💪 Built with passion and dedication

**Made by:** [Shubham Bilgi](https://github.com/Shubhambilgi/)

**Status:** 🚀 In Development | **Day 1/30** ✅

**Last Updated:** September 12, 2026

</div>

---

## 📌 Quick Links

- [Daily Progress](docs/)
- [Day 1 Learnings](docs/Day1-UserModel.md)
- [GitHub Repository](https://github.com/Shubhambilgi/finance-tracker)
- [Project Issues](https://github.com/Shubhambilgi/finance-tracker/issues)

---

**Happy Learning! 🎓 | Keep Building! 🚀 | Share Your Progress! 📈**
