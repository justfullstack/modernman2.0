
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from shop import models
from customauth import forms
from django.core import mail


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
        
        
        
        
        
        
        
class TestCustomAuthViews(TestCase):
    """A test for the custom authentication model's views"""
    
    def testValidSignupFormSendsEmail(self):
        """tests the form sends an email on successful submit"""
        form = forms.CustomUserCreationForm(
                    {
                        "email": "user1234@modernman.com",
                        "password1": "abc@abcabc12!",
                        "password2": "abc@abcabc12!",
                    }
                )
        
        self.assertTrue(form.is_valid())
        
        with self.assertLogs("customauth.forms", level="INFO") as cm:
            form.send_mail()
            
            self.assertEqual(len(mail.outbox), 1)
            
            self.assertEqual(
                    mail.outbox[0].subject, "Welcome to Modernman!"
                )
            
        self.assertGreaterEqual(len(cm.output), 1)
        
        
        
    





