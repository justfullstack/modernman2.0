from django.urls import path, include
from .views import (
                AddressCreateView,
                AddressListView ,
                AddressUpdateView,
                AddressDeleteView,
                )


urlpatterns = [
    
            path(
                'addresses/create/',
                AddressCreateView.as_view(),
                name="create-address"
            ),


            path(
                'addresses/<int:pk>/update/',
                AddressUpdateView.as_view(),
                name="update-address"
            ),

            path(
                'addresses/<int:pk>/delete/',
                AddressDeleteView.as_view(),
                name="delete-address"
            ),

            path(
                'addresses/',
                AddressListView.as_view(),
                name="addresses"
            ),

            
        ]