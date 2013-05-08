from django.db.models.signals import post_save
from order.models import Order


def deliver_digital_on_paid_order(sender, instance, **kwargs):
    if instance.status == 'fully-paid':
        digital_deliveries = instance.groups.filter(digitaldeliverygroup__isnull=False)
        for delivery in digital_deliveries:
            delivery.change_status('shipped')

post_save.connect(deliver_digital_on_paid_order, sender=Order)
