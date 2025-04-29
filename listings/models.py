from django.db import models
from django.contrib.auth.models import User
from core.base_models import BaseModel


class Listing(BaseModel):

    CURRENCY_CHOICES = [
        ('UZS', 'UZS'),
        ('USD', 'USD')
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used')
    ]

    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='listings')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    location = models.CharField(max_length=50)
    condition = models.CharField(max_length=5, choices=CONDITION_CHOICES)
    is_negotiable = models.BooleanField()
    is_active = models.BooleanField()
    is_featured = models.BooleanField()
    views_count = models.PositiveIntegerField()
    expires_at = models.DateTimeField()

class Message(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    is_read = models.BooleanField()

class Review(BaseModel):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_written')
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_received')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()

class PriceHistory(BaseModel):

    CURRENCY_CHOICES = [
        ('UZS', 'UZS'),
        ('USD', 'USD')
    ]

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)