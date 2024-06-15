from . import views 
from django.urls import path  



urlpatterns = [ 

        path(
            "<slug:tag>/",
            views.ProductListView.as_view(),
            name="products",
        ), 
        
        
    ] 