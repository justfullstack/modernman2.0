from django.urls import path
from .views import (addToCart, removeFromCart, ManageCart)

urlpatterns = [ 
    
    path(
        'add-to-cart/<slug:slug>', 
        addToCart,
        name='add-to-cart'
        ),

    path(
        'remove-from-cart/<slug:slug>', 
        removeFromCart,
        name='remove-from-cart'
        ),

    path(
        'cart/', 
        ManageCart.as_view(),
        name='cart'
        ),
]