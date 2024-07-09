from django.urls import path
from .views import addToCart

urlpatterns = [ 
    
    path(
        'add-to-cart/<slug:slug>', 
        addToCart,
        name='add-to-cart'
        ),
]