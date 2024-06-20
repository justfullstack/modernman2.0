from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm 
from django.contrib.auth import forms  
from django.core.mail import send_mail
import logging
from . import models


logger = logging.getLogger(__name__)



class CustomUserCreationForm(DjangoUserCreationForm):
    """A custom user creation form. It replaces the builtin username field to use only the email address."""
    class Meta(DjangoUserCreationForm.Meta):
        """Overrides builtin custom user creation forms."""
        model = models.CustomUser
        fields = ('first_name', 'last_name', "email",)
        field_classes = {"email": forms.UsernameField}
        
    def send_mail(self):
        """Sends a welcome email to a new user""" 
        
        email = self.cleaned_data["email"]
        
        logger.info(f"Sending signup email for email {email}")
                
        message = f"Welcome{email} to Modernman\nEnjoy a world of world-class luxury watches \
                from the comfort of your screen!" 
        
        send_mail(
                "Welcome to Modernman!",
                message,
                "site@modernman.com",
                [email],
                fail_silently=True,
                )




