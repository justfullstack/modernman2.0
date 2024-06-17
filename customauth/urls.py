from  .views import (SignupView)  
from django.urls import path  
 


urlpatterns = [ 
        
         
        path(
            "register/",
            SignupView.as_view(),
            name="register",
        ),  
        
    ] 