from django.db import models
from product.models import Product

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=250)
    location = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid_amount = models.PositiveIntegerField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def is_unpaid(self):
        if self.paid_amount < self.get_total_cost():
            return True

    def get_due_amount(self):
        return self.get_total_cost() - self.paid_amount


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Expenditure(models.Model):
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'expenditure {}'.format(self.id)
