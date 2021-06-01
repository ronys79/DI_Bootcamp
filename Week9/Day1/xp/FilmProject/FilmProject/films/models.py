from django.db import models
import datetime
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
       return self.name

class Film(models.Model):
    title = models.CharField(max_length=80)
    release_date = models.DateField(default=datetime.date.today)
    available_in_countries = models.ManyToManyField(Country, related_name="available_countries")
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category= models.ManyToManyField(Category)
    director = models.ManyToManyField("Director")


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default=" ")

    def __str__(self):
       return f'{self.first_name} {self.last_name}'


