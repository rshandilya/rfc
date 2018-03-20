from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.order_list, name='dashboard'),
    path('order-detail/<int:order_id>',
         views.order_detail,
         name='order_detail'),
    path('customer-detail/<int:customer_id>',
         views.customer_detail,
         name='customer_detail'),
]
