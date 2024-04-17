from django.urls import path, include
from . import views
from django.apps import apps


app_name = 'shop'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('order-items/', views.NewOrderItemsView.as_view(), name='order_items'),

   ]