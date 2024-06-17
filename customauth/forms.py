from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm 
from django.contrib.auth import forms  
from django.core.mail import send_mail
import logging
from . import models


logger = logging.getLogger(__name__)



class CustomUserCreationForm(DjangoUserCreationForm):
    
    class Meta(DjangoUserCreationForm.Meta):
        model = models.User
        fields = ("email",)
        field_classes = {"email": forms.UsernameField}
        
        def send_mail(self):
            logger.info(f"Sending signup email for email {email}")
            
            email = self.cleaned_data["email"]
            
            message = f"Welcome{email}" 
            
            send_mail(
                    "Welcome to BookTime",
                    message,
                    "site@booktime.domain",
                    [email],
                    fail_silently=True,
                    )




