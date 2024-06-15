from django.shortcuts import get_object_or_404, render
from . import models
from django.views.generic import ListView




class ProductListView(ListView):

    template_name = "shop/product_list.html"
    paginate_by = 15

    def get_queryset(self):
        products = models.Product.objects.all()

        # tag = self.kwargs['tag']
        # self.tag = None

        # if tag != "all":
        #     self.tag = get_object_or_404(
        #     models.ProductTag, slug=tag
        #     )
        
        # if self.tag:
        #     products = models.Product.objects.active().filter(
        #     tags=self.tag
        #     )
        # else:
        #     products = models.Product.objects.active()
        
        return products.order_by("name")

        # tag = self.kwargs['tag'] 

        # # get tag from link
        # if tag == "all" or tag == "":
        #     self.tag = None
        #     products = Product.objects.active()
        # else:
        #     self.tag = tag

        # # use tag (if any) to retreive data
        # if self.tag is not None:
        #     products = Product.objects.active().filter(category=self.tag)

        # return products.order_by("name")