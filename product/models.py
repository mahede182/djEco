from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    thumbnail = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    rating_rate = models.DecimalField(max_digits=3, decimal_places=2)
    rating_count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    
    @property
    def related(self):
        # Get all products in same category excluding current product
        return self.category.products.exclude(pk=self.pk)

class Slider(models.Model):
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='banners')
    show = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

