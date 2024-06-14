from django.contrib import admin
from django.utils.html import format_html
from . import models 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'in_stock', 'price',)
    list_filter = ('active', 'in_stock', 'date_updated',)
    list_editable = ('in_stock', 'featured', 'on_sale', 'active',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('slug',)




# register models to the admin
admin.site.register(models.Product)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductImage)