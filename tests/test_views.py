
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from shop import models
from django.contrib import auth
from unittest.mock import patch
from customauth.models import CustomUser
from customauth.forms import CustomUserCreationForm
from accounts.models import Address

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
        
        
        
        
    # def testUserSignupPageSubmissionWorks(self):
    #     """tests a user can succesfully submit a  valid singup form"""
        
    #     # credentials
    #     first_name = "First"
    #     last_name = "Last"
    #     email = "user34@domain.com"
    #     password = "abcabcabc34wq"
        
    #     post_data = {
    #             "first_name": first_name,
    #             "last_name": last_name,
    #             "email": email,
    #             "password": password,  
    #             }
        
    #     signup_url = reverse("register") 
        
    #     response = self.client.post(
    #                                 signup_url, 
    #                                 post_data,
    #                             )
            
            
    #     print(response)
        
    #     created_user = CustomUser.objects.filter(email=email)
    #     print(created_user)
        
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
            
                     
        
class TestAddressPage(TestCase):
    def testCreateAddressStoresUser(self):

        user1 = CustomUser.objects.create_user(
                                            first_name="Three",
                                            last_name="Four",
                                            email="three_four@gmail.com",
                                            password="my_P@ssword!"
                                        )

        post_data = {
                    'title': 'MR.',
                    'name': "First Last",
                    'address': "1st Avenue 3rd Street",
                    'town': 'Kambu',
                    'city': "Makueni",
                    'county': '017',
                    'country': "KE",
                }

        self.client.force_login(user1)

        self.client.post(reverse("create-address"), post_data)
        self.assertTrue(Address.objects.filter(user=user1).exists())
    
    
    
    
    
    # def testAddressListReturnsOnlyOwnAddresses(self):
        # create users
        # user1 = CustomUser.objects.create_user(
        #                                 first_name="First",
        #                                 last_name="Last",
        #                                 email="user@gmail.com",
        #                                 password="my_p@ssword!"
        #                             )

        # user2 = CustomUser.objects.create_user(
        #                                 first_name="User",
        #                                 last_name="Two",
        #                                 email="usertwo@gmail.com",
        #                                 password="my_p@ssword!"
        #                             )

        # create tests address for each user
        # address1 = Address.objects.create(
        #                     # user=user1, 
        #                     name="First Last",
        #                     address="127 Kilimani",
        #                     postal_code = "25431",
        #                     town='Nairobi', 
        #                     city="Nairobi",
        #                     country="KE",
        #                 )

        # address2 = Address.objects.create(
        #                     # user=user2, 
        #                     name="User Two",
        #                     address="127 Kilimani",
        #                     postal_code = "25431",
        #                     town='Nairobi', 
        #                     city="Kisumu",
        #                     country="KE", 
        #                 )
        
        # associate address with user
        # address1.user = user1
        # address2.user = user2

        # print(address1)
        # print(address2)
        
        
        # login one user
        # self.client.force_login(user2)

        # response = self.client.get(reverse("addresses"))
        
                
        # self.assertTemplateUsed("accounts/address_list.html")

        # print(f"Response: {response}")
        
        
        # self.assertEqual(response.status_code, 200)

        # address_list = Address.objects.filter(user=user2)
        # print(address_list)
        # print(response.context["object_list"])

        # self.assertEqual(
        #                 list(response.context["object_list"]),
        #                 list(address_list),
        #             )
        
        
        
        