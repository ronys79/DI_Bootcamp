from django.db import models
from  django.urls import reverse
from category.models import Category
from accounts.models import Account


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

# variation of products if want to implement it
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='pot color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='plant size', is_active=True)

variation_category_choice = (
    ('pot color', 'pot color'),
    ('plant size', 'plant size'),
)

class Variation(models.Model):
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category      = models.CharField(max_length=100, choices=variation_category_choice)
    variation_description   = models.CharField(max_length=100)
    is_active               = models.BooleanField(default=True)
    created_date            = models.DateTimeField(auto_now=True)
    # price                 = models.IntegerField()
    # stock                 = models.IntegerField(default=0)
    stock                   = models.IntegerField(default=0)

    objects = VariationManager()

    def __str__(self):
        return self.variation_description

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'Product Gallery'