from django.db import models
from django.urls import reverse
# Create your models here.

class Carusel(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='carusel/',blank=True,null=True)
    bio=models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='product/',blank=True,null=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=100,choices=(("b","Burgers"),("s","Snacks"),("be","Beverages")))
    def __str__(self):
        return self.title



class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name