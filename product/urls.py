from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('cart-detail', views.cart_detail, name='cart_detail'),
    path('<int:product_id>/add-to-cart/',
         views.cart_add,
         name='cart_add'),
]
