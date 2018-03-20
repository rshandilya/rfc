from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('customer', views.find_customer, name='add-customer'),
    path('register-customer',
         views.add_customer,
         name='register-customer'),
    path('paying-amount', views.add_paying_amount, name='paying-amount'),
    path('create-order', views.order_create, name='create-order'),
]
