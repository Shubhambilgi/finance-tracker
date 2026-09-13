from django.contrib import admin
# Import admin tools

from .models import Transaction, Budget
# Import our models


@admin.register(Transaction)
# Register Transaction model with Django admin
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'type', 'date', 'created_at')
    # Show these columns in list view
    
    list_filter = ('type', 'category', 'date', 'created_at')
    # Add filters on right side
    
    search_fields = ('category', 'description', 'user__email')
    # Search by category, description, or user email
    
    ordering = ('-date',)
    # Newest transactions first
    
    readonly_fields = ('created_at',)
    # Don't allow editing created_at


@admin.register(Budget)
# Register Budget model with Django admin
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'limit', 'month')
    # Show these columns in list view
    
    list_filter = ('category', 'month')
    # Filter by category and month
    
    search_fields = ('category', 'user__email')
    # Search by category or user email
    
    ordering = ('-month',)
    # Newest months first
    
    readonly_fields = ('updated_at',)
    # Don't allow editing updated_at