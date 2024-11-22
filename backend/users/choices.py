from django.db import models

class UserRoles(models.TextChoices):
    FARMER = 'Farmer', 'Farmer'
    BUYER = 'Buyer', 'Buyer'
    ADMIN = 'Admin', 'Admin'

class ProductCategory(models.TextChoices):
    VEGETABLES = 'Vegetables', 'Vegetables'
    FRUITS = 'Fruits', 'Fruits'
    SEEDS = 'Seeds', 'Seeds'
    DAIRY = 'Dairy', 'Dairy'
    MEAT = 'Meat', 'Meat'
    EQUIPMENT = 'Equipment', 'Equipment'

class OrderStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    PROCESSING = 'Processing', 'Processing'
    DELIVERED = 'Delivered', 'Delivered'
    CANCELLED = 'Cancelled', 'Cancelled'

class PaymentStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    COMPLETED = 'Completed', 'Completed'
    FAILED = 'Failed', 'Failed'

class MeasurementUnit(models.TextChoices):
    KG = 'kg', 'kg'
    PACK = 'pack', 'pack'
    LITERS = 'liters', 'liters'
    UNIT = 'unit', 'unit'