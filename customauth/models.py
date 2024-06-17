from django.contrib.auth.models import (
                            AbstractUser,
                            BaseUserManager,
                            )
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    
    use_in_migrations = True
    
    def _create_user(self,first_name,last_name, email, password, **extra_fields):
        
        #  ensure an email address
        if not email:
            raise ValueError("An email address  must be set!")
        
        # ensure at least one name is added
        if not (first_name or last_name):
            raise ValueError(_("At least one name is required!"))
        
        # ensure valid email address
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Invalid email address!"))

 
        email = self.normalize_email(email)
        
        user = self.model(
                    first_name=first_name,
                    last_name=last_name,
                    email=email, 
                    **extra_fields
                    )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self, first_name,last_name,email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        return self._create_user(
                        first_name,
                        last_name,email, 
                        password, 
                        **extra_fields
                        )
    
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if not email:
            raise ValueError(_("Email address is required!")) 
        try:
            validate_email(email) 
        except ValidationError:
            raise ValueError(_("Invalid email address!"))
        
        
        
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        
        # confirm extra fields permissions set succefully
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        
        first_name="Admin"
        last_name=None
                
        superuser = self._create_user(
                            first_name,
                            last_name, 
                            email, 
                            password, 
                            **extra_fields,
                            )
        
        
        return superuser
    
    
    
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    
            
            
        