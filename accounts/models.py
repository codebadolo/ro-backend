from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('inventory', 'Inventory Manager'),
        ('shipping', 'Shipping Manager'),
        ('owner', 'Owner'),
        ('customer_service', 'Customer Service'),
        ('it_support', 'IT Support'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='inventory')

    def __str__(self):
        return self.username
