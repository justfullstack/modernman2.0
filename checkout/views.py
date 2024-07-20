from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from shop.models import Product
from .models import Cart, CartLine
from . import forms
from django.views import View
from django.urls import reverse
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



class ManageCart(View):
    def get(self, request):
        template = 'checkout/cart.html'

        if not request.cart or request.cart.is_empty(): 
            context = {
                    'formset': None, 
                     } 
            
        else: 
            formset = forms.CartLineFormSet(instance=request.cart)  

            subtotal=0
            # subtotal=0 # initialize subtotal
            for form in formset:
                subtotal += form.instance.subtotal()
            
        
            shipping = 0.05 * float(subtotal) 
            vat = 0.15 * float(subtotal)  # vat of 15%

            total = float(subtotal) +  vat  +  shipping

            context = {
                            'formset': formset, 
                            'subtotal': subtotal,
                            'vat': vat,
                            'shipping': shipping,
                            'total': total,
                        }
        
        return render(
                    request,
                    template_name=template,
                    context=context,
                    )


    def post(self, request):
        template = 'checkout/cart.html'
        formset = forms.CartLineFormSet(
                                    request.POST,
                                    instance=request.cart,
                                    )
        
        if formset.is_valid():
            formset.save()


            # update cart figuress
            subtotal=0  # initialize subtotal
           
            for form in formset:
                subtotal += form.instance.subtotal()

            shipping = 0.05 * float(subtotal) 
            vat = 0.15 * float(subtotal)  # vat of 15%

            total = float(subtotal) +  vat  +  shipping

            context = {
                        'formset': formset, 
                        'subtotal': subtotal,
                        'vat': vat,
                        'shipping': shipping,
                        'total': total,
                    }
            
            return render(
                    request,
                    template_name=template,
                    context=context,
                      )
        
        else:
            messages.error(
                        request, 
                        f"{list(formset.errors)}!"
                    )
            # for error in formset.errors:
            #     messages.error(
            #             request, 
            #             f"{error}!"
            #         )


        # else:
        #     messages.error(request, "Could not update cart!")
            
        #     # update cart figuress
        #     subtotal=0  # initialize subtotal
           
        #     for form in formset:
        #         subtotal += form.instance.subtotal()

        #     shipping = 0.05 * float(subtotal) 
        #     vat = 0.15 * float(subtotal)  # vat of 15%

        #     total = float(subtotal) +  vat  +  shipping

        #     context = {
        #                 'formset': formset, 
        #                 'subtotal': subtotal,
        #                 'vat': vat,
        #                 'shipping': shipping,
        #                 'total': total,
        #             }
            
        #     return render(
        #             request,
        #             template_name=template,
        #             context=context,
        #             )
                

        return render(
                    request,
                    template_name=template,
                    context={
                        'formset': formset, 
                    },
                    )
        
            
        
# remove from cart
def removeFromCart(request, slug):
    '''
    adds a product to the cart,  relying on 
    the cart_middleware to position the existing
    basket inside the request.basket attribute
    '''
    
    product = get_object_or_404(
                            Product,
                            slug=slug
                        )

    cart = request.cart

    cartline = CartLine.objects.filter(
        cart=cart,
        product=product
    )

    # if cartline was already initiated
    if not cartline.exists():
        messages.error(request, f" Error removing '{product.name}' from the cart!")
    else:
        cartline.delete()
        # cartline.save()


        messages.error(
            request, f"'{product.name}'  removed from the cart!") 
        
    return redirect(reverse("cart"))


       