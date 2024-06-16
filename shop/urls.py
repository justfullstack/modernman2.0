from . import views 
from django.urls import path  



urlpatterns = [ 

        path(
            "<slug:tag>/",
            views.ProductListView.as_view(template_name = "shop/products_list.html"),
            name="products",
        ), 

        
    ] 