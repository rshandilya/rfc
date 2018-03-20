from django.shortcuts import render, get_object_or_404
from product.cart import Cart
from .forms import CustomerForm
from .models import Order, OrderItem, Customer

# Create your views here.


def order_create(request):
    cart = Cart(request)
    new_order = request.session['order']
    order = Order.objects.create(customer=new_order['customer'],
                                 paid_amount=new_order['paid_amount'])
    for item in cart:
        OrderItem.objects.create(order=order,
                                 product=item['product'],
                                 price=item['price'],
                                 quantity=item['quantity'])
    cart.clear()
    new_order.clear()
    return render(request, 'order/order-created.html')


def find_customer(request):
    cart = Cart(request)
    form = CustomerForm()
    return render(request,
                  'order/add-customer.html',
                  {'cart': cart, 'form': form})


def add_customer(request):
    cart = Cart(request)
    if request.session['order']:
        request.session['order'].clear()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
    else:
        phone_number = request.GET['phone']
        customer = get_object_or_404(Customer, phone_number=phone_number)
    request.session['order'] = {'customer': customer,
                                'paid_amount': ""}
    return render(request, 'order/add-paid-amount.html',
                  {'cart': cart, 'customer': customer})


def add_paying_amount(request):
    paid_amount = request.GET['amount']
    request.session['order']['paid_amount'] = paid_amount
    request.session.modified = True
    new_order = request.session['order']
    cart = Cart(request)
    return render(request,
                  'order/confirm-order.html',
                  {'cart': cart, 'order': new_order})
