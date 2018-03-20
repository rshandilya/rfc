from django.contrib import admin
from .models import Customer, Order, Expenditure

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'location']
admin.site.register(Customer, CustomerAdmin)


class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['amount', 'created', 'description']
admin.site.register(Expenditure, ExpenditureAdmin)

admin.site.register(Order)

