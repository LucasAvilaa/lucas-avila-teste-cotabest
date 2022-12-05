from django.core.exceptions import ValidationError
from django.urls import reverse 
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    minimum = models.IntegerField(default=1)
    amount_per_package = models.IntegerField(default=0)
    max_availability = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product:product_list")

class Cart(models.Model):
    product_id = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.product_id.name

    def get_absolute_url(self):
        return reverse("product:cart_list")
 
    def price(self):
        return self.product_id.price

    def subtotal(self):
        return self.quantity * self.product_id.price

    def minimum(self):
        return self.product_id.minimum
    
    def amount_per_package(self):
        return self.product_id.amount_per_package
    
    def save(self, *args, **kwargs):
        if self.id:
            self.validations()
            return super(Cart, self).save(*args, **kwargs)
        else:
            exist_product = Cart.objects.filter(product_id=self.product_id.id)
            
            if exist_product:
                for p in exist_product:
                    p.quantity += self.quantity
                    p.validations()
                    p.save()
            else:
                self.validations()
                super(Cart, self).save(*args, **kwargs)

    def validations(self):
        if self.quantity < self.product_id.minimum:
            raise ValidationError(f"Minimum valid quantity: {self.product_id.minimum}")

        if self.quantity % self.product_id.amount_per_package:
            raise ValidationError(f"Selected quantity is not compatible with the quantity per package {self.product_id.amount_per_package} of product {self.product_id}")
        
        if self.quantity > self.product_id.max_availability:
            raise ValidationError(f"Quantity greater than available: {self.product_id.max_availability}")