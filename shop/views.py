from django.shortcuts import get_object_or_404, render
from . import models
from django.views.generic import (ListView, DetailView)



class ProductListView(ListView):
    model = models.Product
    template_name = "shop/product_list.html"
    paginate_by = 10

    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag = None
        
        if tag != "all":
            self.tag = get_object_or_404(
                                models.Category, 
                                slug=tag,
                                )
            
        if self.tag:
            products = models.Product.objects.active().filter(tags=self.tag)
        else:
            products = models.Product.objects.active()
            
        
        return products.order_by("name")
    
    
    
class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'shop/product_detail.html'
    
    
    
    
    
    
    
    