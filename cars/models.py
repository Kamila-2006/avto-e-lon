from django.db import models
from django.contrib.auth import get_user_model
from core.base_models import BaseModel
from listings.models import Listing


User = get_user_model()

class Make(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='car-logo/', null=True, blank=True)

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=50)

class Image(BaseModel):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    is_primary = models.BooleanField()
    order = models.PositiveSmallIntegerField()

class BodyType(models.Model):
    name = models.CharField(max_length=50)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, related_name='body_type', null=True, blank=True)

class Feature(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

class SavedListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_listings')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='saved_listings')

class ComparisonList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comparisons')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comparisons')

class Car(BaseModel):

    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('gas', 'Gas (LPG/CNG)'),
        ('hydrogen', 'Hydrogen'),
        ('other', 'Other'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('cvt', 'CVT'),
        ('semi-automatic', 'Semi-Automatic'),
        ('dual-clutch', 'Dual-Clutch'),
        ('other', 'Other'),
    ]

    DRIVE_TYPE_CHOICES = [
        ('front', 'Front'),
        ('rear', 'Rear'),
        ('all', 'All'),
    ]

    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='cars')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars')
    year = models.PositiveIntegerField()
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, related_name='cars')
    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    engine_size = models.FloatField()
    power = models.PositiveIntegerField()
    drive_type = models.CharField(max_length=50, choices=DRIVE_TYPE_CHOICES)
    features = models.ManyToManyField(Feature, related_name='cars')
    vin = models.CharField(max_length=17, unique=True)