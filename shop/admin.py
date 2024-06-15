from django.contrib import admin
from django.utils.html import format_html
from . import models 

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'stock_count', 'price', 'active','slug', 'on_sale','featured', )
    # list_filter = ('active', 'stock_count', 'date_created', 'date_updated','slug', 'on_sale','featured', )
    list_editable = ('stock_count', 'featured', 'on_sale', 'active', )
    search_fields = ('name','categories',)
    prepopulated_fields = {"slug": ("name",)}
    # readonly_fields = ['slug',]
    autocomplete_fields = ('categories',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') 
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'product_name')
    readonly_fields = ('thumbnail',)
    search_fields = ('product__name',)
    
    
    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                        '<img src="%s"/>' % obj.thumbnail.url
                        )
        return "-"
    
    thumbnail_tag.short_description = "Thumbnail"

    def product_name(self, obj):
        return obj.product.name 


# register models to the admin
admin.site.register(models.Product, ProductAdmin) 
admin.site.register(models.ProductImage, ProductImageAdmin )
admin.site.register(models.Category, CategoryAdmin)


