
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from shop import models
from django.contrib import auth
from unittest.mock import patch
from customauth.models import CustomUser
from customauth.forms import CustomUserCreationForm


class TestProductViews(TestCase):
    def testProductsPageReturnsActive(self):
        models.Product.objects.create(
                        name="The Greatest Watch in History",
                        slug="the-greatest-watch-in-history",
                        price=Decimal("132.00"),
                        )
        
        models.Product.objects.create(
                        name="Hublot Leather Premium Watch",
                        slug="hublot-leather-premium-watch",
                        price=Decimal("2.00"),
                        active=False,
                        )
        
        response = self.client.get(
                        reverse("products", 
                                kwargs={"tag": "all"}
                                )
                        )
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Greatest")
        
        product_list = models.Product.objects.active().order_by("name")
        
        self.assertEqual(
                        list(response.context["object_list"]),
                        list(product_list),
                        )
    
                       
    
    def testProductsPageFiltersByTagsAndActive(self):
        product = models.Product.objects.create(
                        name="The Greatest Watch in History",
                        slug="the-greatest-watch-in-history",
                        price=Decimal("132.00"),
                        )
        
        product.categories.create(name="Test Watch Category", slug="test-watch-category") 
        
        models.Product.objects.create(
                        name="Hublot Leather Premium Watch",
                        slug="hublot-leather-premium-watch",
                        price=Decimal("2.00"),
                        active=False,
                        )
        
        response = self.client.get(
                        reverse(
                            "products",
                            kwargs={"tag": "all"}
                            )
                        )
        

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Greatest Watch in History")
        
        product_list = (
                        models.Product.objects.active()
                        .filter(categories__slug="test-watch-category")
                        .order_by("name")
                        )
        
        self.assertEqual(
                        list(response.context["object_list"]),
                        list(product_list),
                        )
        
        
 




class TestAuthPage(TestCase):
    """Tests projects html pages and other frontend functionality for authentication pages"""
    
        
    def testUserSignupPageLoadsCorrectly(self):
        
        signup_url = reverse("register")
        signup_template = "customauth/signup.html"
        
        response = self.client.get(signup_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, signup_template)
        self.assertContains(response, "Join Modernman")
        self.assertIsInstance(
                    response.context["form"], 
                    CustomUserCreationForm
                    )
        
        
        
        
    def testUserSignupPageSubmissionWorks(self):
        """tests a user can succesfully submit a  valid singup form"""
        
        # credentials
        first_name = "First"
        last_name = "Last"
        email = "user34@domain.com"
        password = "abcabcabc34wq"
        
        post_data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,  
                }
        
        signup_url = reverse("register") 
        
        response = self.client.post(
                                    signup_url, 
                                    post_data,
                                )
            
            
        print(response)
        
        created_user = CustomUser.objects.filter(email=email)
        print(created_user)
        
        # with patch.object(CustomUserCreationForm, "send_mail") as mock_send:
        #     response = self.client.post(
        #                             signup_url, 
        #                             post_data,
        #                         )
            
            
        #     print(response)
            
            # response is HTTP 302 - Redirect
            # self.assertEqual(response.status_code, 302)     
            
            # created_user = CustomUser.objects.filter(email=email, password=password) 
            # created_user = CustomUser.objects.get(email=email)
            
            # self.assertTrue(created_user.exists()) 
            
            # print(created_user)
                        
            # confirm new user logged in
            # self.assertTrue(
            #             auth.get_user(self.client).is_authenticated
            #         )
            
            # print(auth.get_user(self.client).is_authenticated )
            
            # mock_send.assert_called_once()
            
            
            
            
            
            
        
        
        