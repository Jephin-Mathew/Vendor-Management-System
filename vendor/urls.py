from django.urls import path
from . import views

urlpatterns = [
    path('simpleapi/', views.simple_api, name='simple_api'),
    # Vendor Profile Management
    path('vendor_create/', views.vendor_create, name='vendor_create'),
    path('vendor_list/', views.vendor_list, name='vendor_list'),
    path('vendor_detail_get/<int:pk>/',
         views.vendor_detail_get, name='vendor_detail_get'),
    path('vendor_detail_put/<int:pk>/',
         views.vendor_detail_put, name='vendor_detail_put'),
    path('vendor_detail_delete/<int:pk>/',
         views.vendor_detail_delete, name='vendor_detail_delete'),
    # Purchase Order Tracking
    path('purchase_order_create/', views.purchase_order_create,
         name='purchase_order_create'),
    path('purchase_order_list/', views.purchase_order_list,
         name='purchase_order_list'),
    path('purchase_order_detail_get/<int:po_id>/',
         views.purchase_order_detail_get, name='purchase_order_detail_get'),
    path('purchase_order_detail_put/<int:po_id>/',
         views.purchase_order_detail_put, name='purchase_order_detail_put'),
    path('purchase_order_detail_delete/<int:po_id>/',
         views.purchase_order_detail_delete, name='purchase_order_detail_delete'),
    # Vendor Performance Evaluation
    path('vendor_performance/<int:vendor_id>/',
         views.vendor_performance, name='vendor_performance'),
    path('acknowledge_purchase_order/<int:po_id>/',
         views.acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
