import datetime
from django.core.urlresolvers import reverse
from django.db import models
from product.models import Product, StockedProduct
import random
import string

CODE_CHARS = string.letters + string.digits
CODE_LENGTH = 24

class CouponCode(models.Model):
    coupon = models.ForeignKey('coupon.Coupon')
    order = models.ForeignKey('order.Order', blank=True, null=True)
    redeemed_on = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=200)

    def can_be_used(self):
        today = datetime.datetime.now()
        if self.coupon.valid_from is not None and self.coupon_valid_from < today:
            return False
        if self.coupon.valid_until is not None and self.coupon_valid_until > today:
            return False
        return self.redeemed_on is None

    def get_absolute_url(self):
        return reverse('coupon:coupon-code-detail', kwargs={'slug': str(self.code)})

    def owner(self):
        return self.order.anonymous_user_email or self.order.user.email

class Coupon(Product, StockedProduct):
    short_description = models.TextField(blank=True, null=True)
    terms = models.TextField(blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_until = models.DateField(blank=True, null=True)

    def email_coupon_code(self, coupon_code):
        print 'send email with %r' % coupon_code

    def deliver(self, order):
        coupon_code = self.create_code(order)
        self.email_coupon_code(coupon_code)

    def generate_coupon_code(self):
        assert self.pk is not None
        return str(self.pk) + "".join(random.choice(CODE_CHARS) for i in xrange(CODE_LENGTH))

    def create_code(self, order):
        code = self.generate_coupon_code()
        return CouponCode.objects.create(
            coupon=self,
            order=order,
            code=code
        )
