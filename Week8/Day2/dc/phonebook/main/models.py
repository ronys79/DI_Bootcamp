from django.db import models

# Create your models here.

class Phonebook(models.Model):
    name = models.CharField(max_length=100, default='a')
    email = models.CharField(max_length =200, unique=True, default="a@gmail.com")
    phone_number = models.IntegerField(default=100)
    address = models.CharField(max_length=100, default='b')