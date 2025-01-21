from django.contrib import admin
from .models import Order, OrderItem

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity']
    list_filter = ['price']
    search_fields = ['product__title']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'paid', 'status', 'created_date']
    list_filter = ['paid', 'status', 'created_date']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['paid', 'status']