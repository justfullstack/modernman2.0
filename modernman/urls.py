import shop
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

import shop 



urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
        ),


    path(
        'products/',
        include('shop.urls'),
        name='products'
    ),  


    path(
        '', 
        TemplateView.as_view(template_name='index.html'),
        name='home'
        ),

     


]   + static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
    )

# serve local media during devt.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
     


       
       
