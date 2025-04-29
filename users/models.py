from django.contrib.auth.models import User
from django.db import models
from core.base_models import BaseModel


class UserProfile(BaseModel):

    USER_CHOICES = [
        ('oddiy', 'Oddiy'),
        ('diler', 'Diler')
    ]

    user_type = models.CharField(max_length=6, choices=USER_CHOICES)
    phone = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    location = models.CharField(max_length=50)
    rating = models.FloatField()

class Dealer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    company_name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='company-logo/', null=True, blank=True)
    website = models.URLField()
    address = models.TextField()
    is_verified = models.BooleanField()
    rating = models.FloatField()