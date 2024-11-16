from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('LoanProvider', 'Loan Provider'),
        ('LoanCustomer', 'Loan Customer'),
        ('BankPersonnel', 'Bank Personnel'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    # Avoid import errors by specifying related_name attributes
    groups = models.ManyToManyField(
        Group,
        related_name='loan_management_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='loan_management_user_permissions',
        blank=True,
    )

# Define the LoanFund model
class LoanFund(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Define the Loan model
class Loan(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    term_months = models.PositiveIntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Define the LoanSettings model
class LoanSettings(models.Model):
    min_amount = models.DecimalField(max_digits=15, decimal_places=2)
    max_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
