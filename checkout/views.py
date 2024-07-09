from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from shop.models import Product
from .models import Cart, CartLine
# Create your views here.



# add to cart
def addToCart(request, slug):
    '''
    adds a product to the cart,  relying on 
    the cart_middleware to position the existing
    basket inside the request.basket attribute
    '''
    # product_slug = request.GET.get("product_slug")

    # product = get_object_or_404(
    #     Product,
    #     slug=slug
    # )

    product = get_object_or_404(
                            Product,
                            # pk=request.GET.get("product_id")
                            slug=slug
    )

    cart = request.cart

    if not cart:
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        cart = Cart.objects.create(user=user)

        request.session["cart_id"] = cart.id

        cart.save()

    (cartline, created) = CartLine.objects.get_or_create(
                                                    cart=cart,
                                                    product=product
                                                )

    # if cartline was already initiated
    if not created:
        messages.warning(request, f"'{product.name}' already in the cart!")

        cartline.quantity += 1 # simply update product count
        messages.info(
                    request, 
                    f" Item quantity updated to {cartline.quantity}!"
                )
        cartline.save()
    else: 
        messages.success(
            request, f"'{product.name}' successfully added to the cart!")

    return redirect("product",  slug=product.slug)

