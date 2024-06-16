from decimal import Decimal
from django.test import TestCase
from shop import models


class TestModel(TestCase):
    def testProductActiveManager(self):
        models.Product.objects.create(
                name="First Product Testing Active Manager",
                price=Decimal("10.00")
                )
        
        models.Product.objects.create(
                name="Second Product Testing Active Manager",
                price=Decimal("2.00")
                )
        
        # not active
        models.Product.objects.create(
                name="Third Product Testing Active Manager",
                price=Decimal("2.00"),
                active=False)
        
        # only two products should be active
        self.assertEqual(len(models.Product.objects.active()), 2)