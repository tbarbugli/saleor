from django.conf.urls import patterns, url
from .views import CouponCodeDetailView

urlpatterns = patterns('',
    url(r'^code/(?P<slug>[a-zA-Z0-9-]+)/$', CouponCodeDetailView.as_view(), name='coupon-code-detail'),
)
