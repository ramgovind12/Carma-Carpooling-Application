from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    
    fuel_choices = [
        ('Petrol', 'Petrol'),
        ('Diesel','Diesel'),
        ('Electric','Electric')
    ]
    
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 15)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    car_name = models.CharField(max_length = 100)
    car_make = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=10, choices = fuel_choices)
    car_image = models.ImageField(upload_to='car_images/')
    
    def __str__(self) -> str:
        return self.name.username
    
class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete = models.CASCADE)
    departure_location = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)
    date = models.DateField() 
    time = models.TimeField()
    available_seats = models.PositiveIntegerField()
    car  = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 8,decimal_places = 2)
    
    def __str__(self) -> str:
        return f"ride from {self.departure_location} to {self.destination}"