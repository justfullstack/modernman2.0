import logging
from django.contrib.auth import login, authenticate
from django.contrib import messages
from . import forms
from django.views.generic import FormView
from django.shortcuts import redirect


logger = logging.getLogger(__name__)


class SignupView(FormView):
    template_name = "customauth/signup.html"
    form_class = forms.CustomUserCreationForm
    
    
    def get_success_url(self):
        
        redirect_to = self.request.GET.get("next", "/products/all")
        return redirect_to 
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        
        logger.info(
                f"New signup for email={email} through SignupView",
                )
        
        user = authenticate(email=email, password=raw_password)
        
        login(self.request, user)
        
        form.send_mail()
        
        messages.success(
                    self.request, "Signed up successfully! Welcome to Modernman."
                    )
        
        return response 
    
    
    
    