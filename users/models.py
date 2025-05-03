from django.contrib.auth.models import AbstractUser
from django.db import models
from core.base_models import BaseModel


class User(AbstractUser):
    USER_CHOICES = [
        ('regular', 'Regular'),
        ('dealer', 'Dealer'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_CHOICES, default='regular')

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    location = models.CharField(max_length=50)
    rating = models.FloatField()

class Dealer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dealer')
    company_name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='company-logo/', null=True, blank=True)
    website = models.URLField()
    address = models.TextField()
    is_verified = models.BooleanField(null=True, blank=True)
    rating = models.FloatField(default=0.00)