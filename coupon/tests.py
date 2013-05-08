"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Coupon
from product.models import Category
from prices import Price
from order.models import Order
from userprofile.models import Address

class TestCoupon(TestCase):

    def setUp(self):
        self.category, c = Category.objects.get_or_create(
            name='test_category'
        )
        self.coupon = Coupon.objects.create(
            name='test_coupon',
            price=Price(1, currency='USD'),
            category=self.category
        )
        self.address = Address.objects.create()

    def test_auto_shipping_order(self):
        order = Order.objects.create(
            billing_address=self.address 
        )
