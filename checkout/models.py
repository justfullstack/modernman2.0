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
        quantity = 0
        for i in self.cartline_set.all():
            quantity += 1
        return quantity 
    


 

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

    # def createOrder(self, billing_address, shipping_address):
    #     '''creates an order from the cotents of the cart'''
    #     if self.user is None:
    #         raise ValueError('Cannot create order without a user! You must be logged in.')

    #     logger.info(
    #         f'Creating order for cart {self.id} , shipping_address_id={shipping_address.id}, billing_address_id={billing_address.id}')

    #     order_data = {
    #         "user": self.user,
    #         "billing_title": billing_address.title,
    #         "billing_name": billing_address.name,
    #         "billing_address": billing_address.address,
    #         "billing_postal_code": billing_address.postal_code,
    #         "billing_town": billing_address.town,
    #         "billing_county": billing_address.county,
    #         "billing_city": billing_address.city,
    #         "billing_country": billing_address.country,
    #         "billing_phone_no": billing_address.phone_no,
    #         "shipping_title": shipping_address.title,
    #         "shipping_name": shipping_address.name,
    #         "shipping_address": shipping_address.address,
    #         "shipping_postal_code": shipping_address.postal_code,
    #         "shipping_town": shipping_address.town,
    #         "shipping_county": shipping_address.county,
    #         "shipping_city": shipping_address.city,
    #         "shipping_country": shipping_address.country,
    #         "shipping_phone_no": shipping_address.phone_no,
    #     }

    #     order = Order.objects.create(**order_data)

    #     lines_count = 0

    #     for line in self.cartline_set.all():
    #         for _ in range(line.quantity):  # **

    #             order_line_data = {
    #                 "order": order,
    #                 "product": line.product
    #             }

    #             OrderLine.objects.create(**order_line_data)
    #             lines_count += 1

    #     logger.info(
    #         f'created order with id {order.id} and lines_count {lines_count}...')

    #     # update current cart's status to submitted
    #     self.status = Cart.SUBMITTED
    #     self.save()
    #     return order














   
# class CartItem(models.Model):
#     cart_id = models.CharField(max_length=50)
#     date_added = models.DateTimeField(auto_now_add=True)
#     quantity = models.IntegerField(default=1)
#     product = models.ForeignKey(Product)

#     class Meta:
#         db_table = 'cart_items'
#         ordering = ['date_added',]

#     def total(self):
#         return self.quantity*self.product.price
    
#     def price(self):
#         return self.product.price
    
#     def name(self):
#         return self.product.name

#     def get_absolute_url(self):
#         return self.product.get_absolute_url()
    
#     def augment_quantity(self, quantity):
#         """used incase the user adds the same product the second time"""
        # self.quantity = self.quantity + int(quantity)
        # self.quantity+=1
        # self.save()


