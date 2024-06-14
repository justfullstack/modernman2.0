from django.contrib import admin
from django.utils.html import format_html
from . import models 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'stock_count', 'price', 'active','on_sale','featured', )
    list_filter = ('active', 'stock_count', 'date_uploaded', 'on_sale','featured', )
    list_editable = ('stock_count', 'featured', 'on_sale', 'active',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    # readonly_fields = ('slug',)


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('active',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ('products',)


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
admin.site.register(models.ProductTag, ProductTagAdmin)
admin.site.register(models.ProductImage, ProductImageAdmin )


