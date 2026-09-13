from django.db import models
# Database ORM tools
from django.conf import settings
# Access Django settings (like AUTH_USER_MODEL)
from decimal import Decimal
# For precise decimal calulations with money

# Define transaction type choices
TRANSACTION_TYPES = [
    ('income', 'Income'), # value stored in database ('income')
    ('expense', 'Expense'), # display name in admin panel ('Income')
]

# Creates a new model called Transaction
class Transaction(models.Model): # Django magic for database table
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    # Link to User
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    # Money with 2 decimal places
    category = models.CharField(max_length=50) 
     # Type of transaction
    description = models.TextField(blank=True, null=True) 
     # Optional details
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='expense') 
     # Income or expense
    date = models.DateField()  
    # When transaction happened
    created_at = models.DateTimeField(auto_now_add=True) 
     # Auto-set when created

   # Str Method  
    def __str__(self):
        return f"{self.category} - ${self.amount} ({self.date})" 
     # Display: groceries - $50.00 (2026-09-12)
    
    # Meta class
    class Meta:
        db_table = 'transactions'  # Database table name
        ordering = ['-date']  # Newest transactions first


# Budget model - spending limits per category per month
class Budget(models.Model):
    # User's budget limit for a spending category in a specific month
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Link to user - each user has their own budgets
    
    category = models.CharField(max_length=50)
    # Budget category (e.g., "groceries", "entertainment")
    
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    # Monthly spending limit amount (e.g., $300.00)
    
    month = models.DateField()
    # Which month is this budget for? (e.g., 2026-09-01 = September 2026)
    
    updated_at = models.DateTimeField(auto_now=True)
    # Auto-updates whenever budget is modified
    
    def __str__(self):
        return f"{self.category} - ${self.limit} ({self.month})"
    # Display: groceries - $300.00 (2026-09-01)
    
    class Meta:
        db_table = 'budgets'
        ordering = ['-month']
        unique_together = ('user', 'category', 'month')
        # Prevent duplicate budgets for same user/category/month combo