from django.db import models
from django.contrib.auth.models import User
from product.models import Product 
from django.conf import settings


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.price * self.quantity
    
    class Meta:
        ordering = ['-id']

class Order(models.Model):
    STATUS = (
        ('RECEIVED', 'Received'),
        ('ON THE WAY', 'On the way'), 
        ('DELIVERED', 'Delivered'),
    )
    PAYMENT_METHODS = (
        ('cod', 'Cash on Delivery'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')  # Updated this line
    order_items = models.ManyToManyField(OrderItem, related_name='orders')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='RECEIVED')
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_total_cost(self):
        total_cost = sum(item.get_total_price() for item in self.items.all())
        return total_cost
