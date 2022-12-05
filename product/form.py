from django import forms 
from product.models import *

class CartModelForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'