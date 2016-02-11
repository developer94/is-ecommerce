from django.contrib import admin
from customer.models import Customer
from customer.forms import CustomerForm

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    exclude = ('details_provided',)

