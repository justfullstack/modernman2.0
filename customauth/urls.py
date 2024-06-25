from  .views import (SignupView)  
from django.urls import path  
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import forms


urlpatterns = [ 
        
         
        path(
            'register/',
            SignupView.as_view(),
            name="register",
        ),  
        
        path(
            'login/',
            auth_views.LoginView.as_view(
                                    template_name="customauth/login.html",
                                    form_class=forms.AuthenticationForm,
                                ),
                name="login",
        ),
        
        path(
            'logout/',
            LogoutView.as_view(),
            name='logout'
        ),
        
    ] 