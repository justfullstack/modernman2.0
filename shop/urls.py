from . import views  
from django.urls import path  
from django.views.generic import DetailView


urlpatterns = [ 
        
         
        path(
            "product/<slug:slug>/",
            views.ProductDetailView.as_view(),
            name="product",
        ), 

        path(
            "<slug:tag>/",
            views.ProductListView.as_view(),
            name="products",
        ), 

        
    ] 