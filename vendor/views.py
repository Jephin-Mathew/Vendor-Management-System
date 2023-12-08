from django.db.models import Avg, Count
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, PurchaseOrder
from datetime import datetime, timedelta, timezone
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django.conf import settings

# Vendor Profile Management

# create


@api_view(['POST'])
@permission_classes([])
def vendor_create(request):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.setdefault('on_time_delivery_rate', 0)
    request.data.setdefault('quality_rating_avg', 0)
    request.data.setdefault('average_response_time', 0)
    request.data.setdefault('fulfillment_rate', 0)

    serializer = VendorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# list


@api_view(['GET'])
def vendor_list(request):
    if auth_token(request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)


# List specific


@api_view(['GET'])
def vendor_detail_get(request, pk):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)


# Update


@api_view(['PUT'])
def vendor_detail_put(request, pk):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)

    request.data.setdefault('on_time_delivery_rate', 0)
    request.data.setdefault('quality_rating_avg', 0)
    request.data.setdefault('average_response_time', 0)
    request.data.setdefault('fulfillment_rate', 0)

    serializer = VendorSerializer(vendor, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete


@api_view(['DELETE'])
def vendor_detail_delete(request, pk):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)

    vendor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Purchase Order Tracking

# create


@api_view(['POST'])
def purchase_order_create(request):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = PurchaseOrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List


@api_view(['GET'])
def purchase_order_list(request):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    vendor_id = request.query_params.get('vendor_id')

    if not vendor_id:
        purchase_orders = PurchaseOrder.objects.all()
    else:
        purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id)

    serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    return Response(serializer.data)


# details


@api_view(['GET'])
def purchase_order_detail_get(request, po_id):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

# update order details


@api_view(['PUT'])
def purchase_order_detail_put(request, po_id):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PurchaseOrderSerializer(purchase_order, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete


@api_view(['DELETE'])
def purchase_order_detail_delete(request, po_id):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

    purchase_order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Vendor Performance Evaluation


@api_view(['GET'])
def vendor_performance(request, vendor_id):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    on_time_deliveries = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        is_on_time_delivery=True
    ).count()

    total_completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed'
    ).count()

    on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * \
        100 if total_completed_orders != 0 else 0

    avg_quality = avg_quality_rating(vendor)
    avg_response = avg_response_time(vendor)
    fulfilment = fulfilment_rate(vendor)

    return Response({
        'on_time_delivery_rate': on_time_delivery_rate,
        'avg_quality': avg_quality,
        'avg_response': avg_response,
        'fulfilment': fulfilment,
    })

# Update Acknowledgment Endpoint


@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    if not auth_token(request):
        return Response({'error': 'Unauthorized token'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

    purchase_order.acknowledgment_date = datetime.now()
    purchase_order.save()
    return Response({'success': 'Purchase order acknowledged successfully'})

# metrics


def avg_quality_rating(vendor):
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed', quality_rating__isnull=False)
    total_quality_rating = completed_orders.aggregate(
        Avg('quality_rating'))['quality_rating__avg']
    return total_quality_rating or 0


def avg_response_time(vendor):
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor,
        status='completed',
        acknowledgment_date__isnull=False,
        issue_date__isnull=False
    )

    total_response_time = sum(
        (
            datetime.combine(
                order.acknowledgment_date,
                datetime.min.time(),
                tzinfo=timezone.utc
            )
            - order.issue_date
        ).days
        for order in completed_orders
    )

    total_completed_orders = completed_orders.count()

    if total_completed_orders != 0:
        average_response_time = total_response_time / total_completed_orders
    else:
        average_response_time = 0

    vendor.average_response_time = average_response_time
    vendor.save()

    return vendor.average_response_time


def fulfilment_rate(vendor):
    fulfilled_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed', issue_date__isnull=False)
    total_orders = PurchaseOrder.objects.filter(
        vendor=vendor,
        issue_date__isnull=False
    ).count()

    if total_orders != 0:
        fulfillment_rate = (fulfilled_orders.count() / total_orders) * 100
    else:
        fulfillment_rate = 0

    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()


# Authentication
def auth_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Token '):
        return False
    token = auth_header.split(' ')[1]
    if token == 'a74336a3ea0b76239abd630e2bda5142d7f12972':
        return True
    else:
        return False
