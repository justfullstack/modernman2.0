from django.contrib.auth.models import (
                                    BaseUserManager, 
                                    AbstractBaseUser,
                                    PermissionsMixin,
                                    )
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import Group


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
        
         
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        
        # confirm extra fields permissions set succefully
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        
        if extra_fields.get("is_active") is not True:
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
    
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """A custom user authentication model"""
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    
    
    objects = CustomUserManager()
    
    first_name = models.CharField(
                            'first_name',
                            max_length=30,
                            null=True,
                            blank=True
                        )

    last_name = models.CharField(
                            'last_name',
                            max_length=30,
                            null=True,
                            blank=True
                        )
    
    email = models.EmailField(
                            'email address',
                            max_length=200,
                            unique=True
                        )

    password = models.TextField(
                            'password',
                            max_length=150,
                            null=True,
                            blank=True
                        )

    avatar = models.ImageField(
                            null=True, 
                            blank=True, 
                            upload_to="media/avatars/",
                            default="media/avatars/default-avatar.png",
                            )

    date_joined = models.DateTimeField(
                            'date_joined', 
                            default=timezone.now
                        )

    last_login = models.DateTimeField(
                            'last_login',
                            null=True,
                            blank=True, 
                        )

    is_subscribed = models.BooleanField(
                            'is_subscribed',
                            default=False,
                            blank=True
                        )

    is_active = models.BooleanField(
                            default=False,
                            null=True,
                            blank=True
                        )

    is_superuser = models.BooleanField(
                            default=False,
                            null=True,
                            blank=True
                        )

    is_admin = models.BooleanField(
                            default=False,
                            null=True,
                            blank=True
                        )

    is_staff = models.BooleanField(
                            default=False,
                            null=True,
                            blank=True
                        )

    is_employee = models.BooleanField(
                            default=False,
                            null=True,
                            blank=True
                        )
    
    groups = models.ManyToManyField(
                            Group,  
                            blank=True,
      
    )
    
    
    # REQUIRED_FIELDS = []
    
    
    def __str__(self):
        if self.first_name or self.last_name:
            the_str = f'{self.email}({self.first_name} {self.last_name})'
        else:
            the_str = f'{self.email})'
            
        return the_str
    
    
            
            
        