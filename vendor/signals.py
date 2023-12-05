from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from .views import calculate_on_time_delivery_rate, avg_quality_rating, avg_response_time, fulfilment_rate


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    calculate_on_time_delivery_rate(
        instance.vendor, instance.is_on_time_delivery)
    avg_quality = avg_quality_rating(instance.vendor)
    avg_response = avg_response_time(instance.vendor)
    fulfilment = fulfilment_rate(instance.vendor)
