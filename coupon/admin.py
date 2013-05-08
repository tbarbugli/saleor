from django.contrib import admin
from .models import Coupon, CouponCode

class CouponCodeInlineAdmin(admin.TabularInline):
    model = CouponCode
    readonly_fields = ['coupon', 'owner','code', 'redeemed_on']
    can_delete = False
    extra = 0

class CouponAdmin(admin.ModelAdmin):
    inlines = [CouponCodeInlineAdmin]

admin.site.register(Coupon, CouponAdmin)
