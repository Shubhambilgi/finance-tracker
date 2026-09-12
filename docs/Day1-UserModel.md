# Day 1: Custom User Model & Admin Setup

## 🎯 What I Built Today

- ✅ Custom User model with email-based authentication
- ✅ CustomUserManager for login
- ✅ Django admin integration
- ✅ Database migrations
- ✅ User testing in Django shell

---

## 📚 What I Learned

### Custom User Model
**Why?**
- Django's default User uses username (we want email)
- Email is unique identifier
- Industry best practice
- More flexible for future

**How?**
- Extend AbstractUser
- Create CustomUserManager
- Set USERNAME_FIELD = 'email'
- Set REQUIRED_FIELDS

### AbstractUser vs BaseUser
| Feature | AbstractUser | BaseUser |
|---------|-------------|----------|
| **Username** | ✅ Included | ❌ No |
| **Password** | ✅ Included | ✅ Included |
| **Email** | ✅ Included | ❌ No |
| **Use Case** | Most apps | Highly custom |

**We used:** AbstractUser (right choice!)

---

## 🔧 Code Breakdown

### CustomUserManager

**Purpose:** Manages user creation without requiring username

```python
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Check email is provided
        if not email:
            raise ValueError('Email is required')
        
        # Normalize email (lowercase, etc)
        email = self.normalize_email(email)
        
        # Create user object
        user = self.model(email=email, **extra_fields)
        
        # Hash password (never store plain text!)
        user.set_password(password)
        
        # Save to database
        user.save(using=self._db)
        
        return user
```

**Key Points:**
- `if not email` → Validation (email required)
- `normalize_email()` → Standardize format
- `set_password()` → Hash password (security!)
- `save()` → Persist to database

### User Model

```python
class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()  # Use custom manager
    
    USERNAME_FIELD = 'email'  # Login with email
    REQUIRED_FIELDS = ['first_name', 'last_name']
```

**Field Explanations:**
- `EmailField(unique=True)` → No duplicate emails
- `auto_now_add=True` → Set once when created (never changes)
- `auto_now=True` → Auto-update on every save
- `USERNAME_FIELD = 'email'` → Use email for login

---

## 🧪 Testing in Shell

### Create User

```python
from users.models import User

test_user = User.objects.create_user(
    email='shubham@example.com',
    password='testpass123',
    first_name='Shubham',
    last_name='Bilgi'
)
```

**What Happens:**
1. CustomUserManager.create_user() called
2. Email validated and normalized
3. Password hashed (bcrypt algorithm)
4. User object created
5. Saved to database
6. Returns user instance

### Verify User

```python
print(test_user.email)           # shubham@example.com
print(test_user.first_name)      # Shubham
print(test_user.created_at)      # 2026-09-12 10:09:50...
```

---

## 🖼️ Screenshots

### Admin Panel
![Admin Panel](screenshots/Day1-admin-panel.png)

**What This Shows:**
- Django admin dashboard
- Users section visible
- Can manage users via GUI
- Filters and search working

### Shell Testing
![Shell Test](screenshots/Day1-shell-user-test.png)

**What This Shows:**
- User created successfully
- Email stored correctly
- created_at timestamp auto-set
- QuerySet shows user instance

---

## 🚨 Issues & Solutions

### Issue 1: NameError - BaseUserManager not imported
**Problem:** `NameError: name 'BaseUserManager' is not defined`

**Solution:** Check imports
```python
from django.contrib.auth.models import AbstractUser, BaseUserManager
```

### Issue 2: InconsistentMigrationHistory
**Problem:** Old migrations conflicted with custom user model

**Solution:** Reset database
```bash
del db.sqlite3
del users\migrations\0001_initial.py
python manage.py makemigrations
python manage.py migrate
```

---

## ✅ Day 1 Checklist

- [x] Created GitHub repository
- [x] Setup Django project
- [x] Created custom User model
- [x] Implemented CustomUserManager
- [x] Configured settings.py
- [x] Created migrations
- [x] Applied migrations
- [x] Created superuser
- [x] Registered in admin
- [x] Tested in shell
- [x] Viewed admin panel
- [x] First git commit

---

## 🎓 Key Takeaways

1. **Email-based auth** is better than username for modern apps
2. **Custom managers** give you control over object creation
3. **Migrations** are Django's way of managing database changes
4. **Admin panel** is powerful for development & testing
5. **Timestamps** are important for tracking data

---

## 📚 Resources Used

- Django Docs: https://docs.djangoproject.com/en/6.1/topics/auth/customizing/
- AbstractUser: https://docs.djangoproject.com/en/6.1/ref/contrib/auth/#abstractuser
- BaseUserManager: https://docs.djangoproject.com/en/6.1/ref/contrib/auth/#baseusermanager

---

## 🚀 Tomorrow (Day 2)

- Create Transaction model
- Create Budget model
- Write serializers
- Create API endpoints
- Test with Postman

---

## 💭 Personal Notes

This was my first deep dive into Django's authentication system. Understanding why we extend AbstractUser and create a custom manager really helped me see how Django's ORM works. The key insight: managers control HOW objects are created, models define WHAT data is stored.

Next goal: Build the REST API so frontend can talk to backend! 🚀

---

**Status:** Day 1 Complete ✅  
**Code commits:** 1  
**Files created:** 15+  
**Lines of code:** ~300  
**Learning time:** ~4 hours  

---

```
🎉 DAY 1: COMPLETE! 🎉
```