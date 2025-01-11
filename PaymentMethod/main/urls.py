from django.urls import path
from .views import *

urlpatterns = [
      path('',Products_page,name = 'products'),
      path('payment/',payment_page,name = 'payment'),
      path('product/<str:name>/<int:id>/',DetailPage,name = 'detail'),
      path('success/',payment_success,name='success'),
      path('cancel/',payment_cancel,name='cancel'),
      ]