from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
