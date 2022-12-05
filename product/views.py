import sys
from product.models import *
from product.serialize import *
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from django.views.generic import *
from product.form import *

""" ==============================================
                    Viewsets
==============================================="""

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


""" ==============================================
                    Product
==============================================="""

class ProductListView(ListView):
    context_object_name = 'products'
    template_name = 'product/product_list.html'
    queryset = Product.objects.all

    def get_queryset(self):
        filter_prod = self.request.GET.get("product")
        if filter_prod:
            products = Product.objects.filter(name__icontains=filter_prod)
        else:
            products = Product.objects.all

        return products

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs.get('pk'))

class ProductCreateView(CreateView):
    form_class = ProductModelForm
    template_name = 'product/product_create.html'
    queryset = Product.objects.all() 

class ProductUpdateView(UpdateView): 
    form_class = ProductModelForm
    template_name = 'product/product_create.html'

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs.get('pk'))

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = "/"


""" ==============================================
                    Cart
==============================================="""

class CartListView(ListView):
    context_object_name = "cart"
    template_name = 'cart/cart_list.html'
    queryset = Cart.objects.all()

class CartDetailView(DetailView):
    template_name = 'cart/cart_detail.html'

    def get_object(self):
        return get_object_or_404(Cart, id=self.kwargs.get('pk'))

class CartCreateView(CreateView): 
    form_class = CartModelForm
    template_name = 'cart/cart_create.html'
    queryset = Cart.objects.all()

class CartUpdateView(UpdateView): 
    form_class = CartModelForm
    template_name = 'cart/cart_create.html'

    def get_queryset(self):
        return Cart.objects.filter(pk=self.kwargs.get('pk'))

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart/cart_confirm_delete.html'
    success_url = "/cart"

def finalize_purchase(request):
    Cart.objects.all().delete()
    return render(request, 'cart/cart_list.html')

def handler500(request, *args, **argv):
    traceback = sys.exc_info()[1]
    try:
        context = {'error': list(traceback)[0]}
    except:
        context = {'error': traceback}

    return render(request, "errors/500.html", context)