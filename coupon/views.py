from django.views.generic import DetailView
from .models import CouponCode

class CouponCodeDetailView(DetailView):
    queryset = CouponCode.objects.all()
    slug_field = 'code'

