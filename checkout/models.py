import logging
from django.db import models
from customauth.models import CustomUser




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
