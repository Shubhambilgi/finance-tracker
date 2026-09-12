from django.contrib import admin
# Import admin tools

from .models import User 
# from .models import User


@admin.register(User) # Tells Django:"Register this model with the admin"
class UserAdmin(admin.ModelAdmin): # Creates an admin interface for User
    list_display = ('email', 'first_name', 'last_name', 'created_at')
    # Shows these columns in the user list
    list_filter = ('created_at', 'is_staff', 'is_superuser')
    # Adds filters on the right side
    search_fields = ('email', 'first_name', 'last_name')
    # Lets you search users by email or name
    ordering = ('-created_at',)
    # Sort by created_at (neweset first), '-' means descending order 
    
    fieldsets = (
        ('User Info', {
            'fields': ('email', 'first_name', 'last_name', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'last_login')
        }),
    )
    # Organizes form fields into sections
    # When editing a user, groups related fields together