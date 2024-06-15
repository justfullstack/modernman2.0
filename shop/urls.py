import shop
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView



urlpatterns = [ 

    path(
        '', 
        TemplateView.as_view(template_name='index.html'),
        name='home'
        ), 
] 