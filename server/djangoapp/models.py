from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('FORD_GT', 'Ford GT'),
        ('MAZDA_RX7', 'Mazda RX7'),
        ('MAZDA_RX8', 'Mazda RX8'),
        ('TOYOTA_COROLLA_SPRINTER_TRUENO_GT_APEX', 'Toyota Corolla Sprinter Trueno GT-APEX'),
    ]
    type = models.CharField(max_length=50, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    def __str__(self):
        return self.name
