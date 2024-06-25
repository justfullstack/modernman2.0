import logging
from django.core import validators
from django.core.mail import send_mail
from django import forms
from django.contrib.auth import authenticate


logger = logging.getLogger(__name__)


class CustomUserCreationForm(forms.Form):
    """
    A form to create a new user, with no privileges, from the given username and password.
    """

    first_name = forms.CharField(
        label='First Name',
        max_length=20,
        required=False, 
    )

    last_name = forms.CharField(
        label='Last Name',
        max_length=20,
        required=False, 
    )

    email = forms.EmailField(
        label='Enter a valid email',
        max_length=200,
        required=True,
        validators=[validators.validate_email, ],
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(render_value=False),
        min_length=8,
        max_length=60,
        required=True
    )

    password2 = forms.CharField(
        label='Repeat Password',
        strip=False,
        widget=forms.PasswordInput(render_value=False),
        min_length=8,
        max_length=60,
        required=True
    )

 

    def clean(self):
        # enforce passwords
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Both passwords must match!")
        else:
            raise forms.ValidationError("Both passwords are required!")
        
        
        
        # enforce at least one name
        if not (self.cleaned_data.get("first_name") or  self.cleaned_data.get("last_name")) : 
            raise forms.ValidationError("At least one name is required!") 
            
            
        return self.cleaned_data
    

    def send_mail(self):
        logger.info(f"Sending signup email for {self.cleaned_data['email']}")
        
        first_name = f"{self.cleaned_data['first_name']}" if self.cleaned_data['first_name'] else ''
        last_name = f"{self.cleaned_data['last_name']}" if self.cleaned_data['last_name'] else ''
        
        name = first_name + ' ' + last_name
        
        from_email = 'welcome@modernman.com'
        to_email = self.cleaned_data["email"]
        subject = 'Welcome to Modernman'
        message = f"Hi {name.title()},\nThank you for joining Modernman, the store of choice for every stylish modern man.Experience the best quality and cost in the market. Please check your inbox for an activation email."

        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[to_email, ],
            fail_silently=False,
            html_message=None
        )

        logger.info(
            f"Signup email successfully sent to {self.cleaned_data['email']}")




    # css classes
    for field in [first_name, last_name, email, password1, password2, ]:
        field.widget.attrs.update({'class': 'form-control'})

    for field in [first_name, last_name, email, password1, password2, ]:
        field.widget.attrs.update({'placeholder': field.label})
        
        
        
        
class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
                        strip=False, 
                        widget=forms.PasswordInput
                        )
    
    def __init__(self, request=None, *args, **kwargs):
        """
        overrides the __init__() method to accept the request object. 
        The request object will be used in the validation because the 
        authenticate() function requires it.
        """
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
        
        
    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        
        # if email is not None and password:
        if email  and password:
            self.user = authenticate(
                                self.request, 
                                email=email, 
                                password=password
                            )
        
            if self.user is None:
                raise forms.ValidationError(
                                "Invalid email/password combination."
                                )
            else:
                logger.info(f"Authentication successful for email={email}" )
            
        return self.cleaned_data
    
    
    def get_user(self):
        return self.user