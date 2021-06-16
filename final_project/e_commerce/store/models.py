from django.db import models
from  django.urls import reverse
from category.models import Category


class Product(models.Model):
    product_name    = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=200, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
#validation for admin/staff before publishing: if upload new product default to not instock+unavailable
    stock           = models.IntegerField(default=0)
    is_available    = models.BooleanField(default=False)
#  If category is deleted the products within it will all be deleted *CAREFUL*
# also linked to caregories so will populate an add button to add more categories from this view
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

# variation of products
# class variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     variation_category = models.CharField(max_length=100), choices= variation_category_choices,