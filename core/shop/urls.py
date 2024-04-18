from django.urls import path, include
from . import views
from django.apps import apps


app_name = 'shop'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('order-items/', views.NewOrderItemsView.as_view(), name='order_items'),
    path('order-customer/<int:order_id>/', views.NewOrderCustomerView.as_view(), name='add_customer'),
    path('select-customer/<int:order_id>/<int:customer_id>/', views.SelectOrderCustomerView.as_view(), name='select_customer'),
    path('order-payment/<int:order_id>/', views.PaymentDetailView.as_view(), name='order_payment'),

   ]