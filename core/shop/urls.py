from django.urls import path, include
from . import views
from django.apps import apps


urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

   ]