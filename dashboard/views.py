from django.shortcuts import render, get_object_or_404
from order.models import Order, Customer

# Create your views here.


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'dashboard/order-history.html', {'orders': orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'dashboard/order-detail.html', {'order': order})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = customer.orders.all()
    return render(request,
                  'dashboard/customer-detail.html',
                  {'customer': customer, 'orders': orders})
