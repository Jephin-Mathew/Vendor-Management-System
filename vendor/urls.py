from django.urls import path
from . import views

urlpatterns = [
    path('simpleapi/', views.simple_api, name='simple_api'),
    # Vendor Profile Management
    path('vendor/create/', views.vendor_create, name='vendor_create'),
    path('vendor/', views.vendor_list, name='vendor_list'),
    path('vendor/<int:pk>/',
         views.vendor_detail_get, name='vendor_detail_get'),
    path('vendor/<int:pk>/edit/',
         views.vendor_detail_put, name='vendor_detail_put'),
    path('vendor/<int:pk>/delete/',
         views.vendor_detail_delete, name='vendor_detail_delete'),
    # Purchase Order Tracking
    path('purchase_order/create/', views.purchase_order_create,
         name='purchase_order_create'),
    path('purchase_order/', views.purchase_order_list,
         name='purchase_order_list'),
    path('purchase_order/<int:po_id>/',
         views.purchase_order_detail_get, name='purchase_order_detail_get'),
    path('purchase_order/<int:po_id>/edit/',
         views.purchase_order_detail_put, name='purchase_order_detail_put'),
    path('purchase_order/<int:po_id>/delete/',
         views.purchase_order_detail_delete, name='purchase_order_detail_delete'),
    # Vendor Performance Evaluation
    path('vendor/<int:vendor_id>/performance/',
         views.vendor_performance, name='vendor_performance'),
    path('purchase_order/<int:po_id>/acknowledge/',
         views.acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
