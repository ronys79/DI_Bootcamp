from django.db import models

# Create your models here.
class Category_Model(models.Model):
    name = models.CharField(max_length=100, default='a')

class Gif_Model(models.Model):
    title = models.CharField(max_length=100, default='a')
    url = models.URLField(max_length =200, default="www.google.com")
    uploader_name = models.CharField(max_length=100, default='b')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category_Model, related_name='gif_category')
