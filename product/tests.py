from product.models import *
from django.test import TestCase

class TestModel(TestCase):
    
    def setUp(self):
        Product.objects.create(
            name="Soda", 
            price=10, 
            minimum=10,
            amount_per_package= 2,
            max_availability=7000)

    """ ===========================================
                    TEST PRODUCTS
    =========================================== """ 
    def test_product_validate_price(self):
        product = Product.objects.get(name="Soda")

        self.assertEqual(product.price, 10)

    def test_product_validate_name(self):
        product = Product.objects.get(name="Soda")

        self.assertGreater(product.max_availability, 500)

    def test_product_change_name(self):
        product = Product.objects.get(name="Soda")
        product.name = "Rice"
        
        self.assertNotEqual(product.name, "Soda")

    def test_product_blank_field(self):
        product = Product.objects.get(name="Soda")
        product.amount_per_package = False

        self.assertFalse(product.amount_per_package)


    """ ===========================================
                    TEST CART 
    =========================================== """ 
    def test_qtd_less_max_availability(self):
        product = Product.objects.get(name="Soda")
        
        cart = Cart.objects.create(
            product_id=product,
            quantity=10
        )
        self.assertLess(cart.quantity, product.max_availability)
    
    def test_qtd_is_not_multiple_of_amount_per_package(self):
        product = Product.objects.get(name="Soda")
       
        with self.assertRaises(ValidationError):
            Cart.objects.create(
            product_id=product,
            quantity=11
        )
    
    def test_qtd_is_less_than_minimum_required(self):
        product = Product.objects.get(name="Soda")
       
        with self.assertRaises(ValidationError):
            Cart.objects.create(
            product_id=product,
            quantity=9
        )
    
    def test_qtd_larger_than_available(self):
        product = Product.objects.get(name="Soda")
        
        with self.assertRaises(ValidationError):
            Cart.objects.create(
            product_id=product,
            quantity=8000
        )