
from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.utils import timezone
from django.urls import reverse 
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site   
from django.urls import reverse 
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from customauth.forms import CustomUserCreationForm
import logging
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView as DjangoLoginView


from customauth.models import CustomUser

logger = logging.getLogger(__name__)


class SignupView(View):

    def get(self, request):

        form = CustomUserCreationForm()

        return render(
                    request, 
                    "customauth/signup.html", 
                    {"form": form}
                )
    

    def post(self, request):

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            
            # gather data
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password1"]

            # ensure user does not already exist
            try:
                CustomUser.objects.get(email=email)
                messages.error(request, "Email address already registered!")

            except CustomUser.DoesNotExist:

                # create user
                user = CustomUser.objects.create_user(  
                                                first_name=first_name.title(),
                                                last_name=last_name.title(),
                                                email=email,
                                                password=password, 
                                            )

                # no activation will be required
                user.is_active = True 

                # send welcome email
                form.send_mail()
                
                # save user
                user.save()


                messages.success(request, "You signed up successfully!")
                
                logger.info(f"Account created successfully for email={email}...!")
                
                
                # login new user
                user_to_login = authenticate(
                                    email=email,
                                    password=password, 
                                )
                
                # print(f"User: {user}")
                # print(f"User to log in: {user_to_login}") 
                
                try: 
                    login(request, user_to_login)
                    logger.info(f"Successfully logged in new user email={email}...!")
                    
                except Exception as e:
                    logger.error(f"Could not log in new user -  {e}") 
        
            return redirect("products", "all") 
        return redirect(reverse("products", "all"))
    


class LoginView(DjangoLoginView):
    
    def get_success_url(self):
        messages.success(self.request, "You are now logged in!") 
        # return reverse( "products", kwargs={'tag': 'all'}) 
        return reverse("products", "all") 