from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse 
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
 
class ActiveManager(models.Manager):
    # allows for query: Product.objects.active()
    def active(self):
        return self.filter(active=True)
    




class Product(models.Model):

    # links active manager to the model
    objects = ActiveManager()
 
    name = models.CharField(max_length=64) 
    description = models.TextField(blank=True)
    price = models.IntegerField(
                blank=False, 
                default=0, 
                validators=[MinValueValidator(0, 'Price cannot be negative!'),]
                )  
    stock_count = models.IntegerField(
                blank=False, 
                default=1
                )
    slug = models.SlugField(
                max_length=48, 
                unique=True,  
                )
    active = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    date_uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(
            Product, 
            blank=True,
            on_delete=models.CASCADE
            )
    image = models.ImageField(
            upload_to="product_images"
            ) 


class ProductImage(models.Model): 
    """web clients images that are too big, because the loading time will be too high"""
    thumbnail = models.ImageField(
            upload_to="product-thumbnails", 
            null=True
            )


class ProductTag(models.Model):
    products = models.ManyToManyField(
            Product, 
            blank=True
            )
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)































