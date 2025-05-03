from django.contrib import admin
from .models import Car, Make, Model, BodyType, Feature


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'logo')

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'name')

@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'body_type', 'fuel_type', 'transmission', 'color', 'mileage', 'engine_size', 'power', 'drive_type', 'vin')