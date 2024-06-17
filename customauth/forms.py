from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm 
from django.contrib.auth import forms  
from django.core.mail import send_mail
import logging
from . import models


logger = logging.getLogger(__name__)



class CustomUserCreationForm(DjangoUserCreationForm):
    
    class Meta(DjangoUserCreationForm.Meta):
        model = models.CustomUser
        fields = ('first_name', 'last_name', "email",)
        field_classes = {"email": forms.UsernameField}
        
    def send_mail(self):
        
        email = self.cleaned_data["email"]
        
        logger.info(f"Sending signup email for email {email}")
                
        message = f"Welcome{email}" 
        
        send_mail(
                "Welcome to Modernman\nEnjoy a world of world-class luxury watches from the comfort of your screen!",
                message,
                "site@modernman.com",
                [email],
                fail_silently=True,
                )




