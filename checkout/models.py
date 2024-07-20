import logging
from django.db import models
from customauth.models import CustomUser
from shop.models import Product
from django.core.validators import MinValueValidator



logger = logging.getLogger(__name__)



class Cart(models.Model):
    """a cart for a user=user or user=None if not authenticated"""

    OPEN = 10
    SUBMITTED = 20

    STATUSES = [
        (OPEN, "Open"),
        (SUBMITTED, "Submitted")
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    status = models.IntegerField(
        choices=STATUSES,
        default=OPEN
    )

    def is_empty(self):
        return self.cartline_set.all().count() == 0
    

    def count(self): 
        return self.cartline_set.all().count()
    

 

class CartLine(models.Model):
    """CartLine model will then connect to a specific product and have an extra field called quantity to store how many of this product are in the basket.
    """
    cart = models.ForeignKey(
                            Cart, 
                            on_delete=models.CASCADE
                            )
    product = models.ForeignKey(
                            Product, 
                            on_delete=models.CASCADE
                            )
    quantity = models.PositiveIntegerField(
                            default=1, 
                            validators=[MinValueValidator(1)]
                            )
    
    def subtotal(self):
        return self.product.price * self.quantity

  