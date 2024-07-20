from django.db import models
from django.urls import reverse 
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
 
class ActiveManager(models.Manager):
    # allows for query: Product.objects.active()
    def active(self):
        return self.filter(active=True)
    

class Category(models.Model): 
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=200,
                        db_index=True,
                        unique=True,
                        blank=True,  
                        null=True,
                        )
    description = models.TextField(blank=True, default='')  

    def __str__(self):
        return self.name.title()
    
    def natural_key(self):
        return (self.slug,)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Product(models.Model):

    # links active manager to the model
    objects = ActiveManager()
 
    name = models.CharField(
                max_length=200,
                db_index=True,
                ) 
    
    description = models.TextField(blank=True)

    price = models.DecimalField(
                max_digits=10, 
                decimal_places=2,
                )
                
    stock_count = models.PositiveIntegerField(
                blank=False, 
                default=1,
                )
    
    slug = models.SlugField(
                max_length=200,
                db_index=True, 
                blank=True,  
                null=True,
                )
    
    active = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    featured = models.BooleanField(default=False) 

    date_created = models.DateTimeField(
                auto_now_add=True,
                null=True,
                )
    
    date_updated = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category)
    
   

    def __str__(self):
        return self.name.title()
    
    def in_stock(self):
        return self.stock_count > 0
    
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('name',) 
        index_together = (('id', 'slug'),)
 
 
class ProductImage(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="product_images")

    thumbnail = models.ImageField(
                        upload_to="product-thumbnails", 
                        null=True,
                        )

    def __str__(self):
        return self.product.name.title()











  