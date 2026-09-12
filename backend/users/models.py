from django.db import models
# Gives us tools like: CharField, EmailField, DateTimeField

from django.contrib.auth.models import AbstractUser, BaseUserManager
# Gives us the base User model we're extending

from django.utils import timezone
# Gives us timezone support for timestamps

class CustomUserManager(BaseUserManager): # Creates a custom manager 
    """
    Custom manager for User model.
    Uses email instead of username for authentication.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with email and password.
        """
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    # Takes email and password as parameters
    # Validates email is provided
    # Normalizes email (lowercase, etc)
    # Hashes password securely
    # Saves to database
    # Returns the user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
    # Creates admin users
    # Sets is_staff and is_superuser to True
    # Calls create_user to do the actual creation


class User(AbstractUser):
#class User(AbstractUser) is the Extend Django's user
    email = models.EmailField(unique=True)
    # Email must be unique
    created_at = models.DateTimeField(auto_now_add=True)
    # Set once When created
    updated_at = models.DateTimeField(auto_now=True)
    # Updates every change

    # Use custom manager
    objects = CustomUserManager()

    # Use email as unique identifier (not username) 

    def __str__(self): #(__str__): Show email in admin
        return self.email
    
    class Meta: #(Meta): Database Configuration
        db_table = 'users'