from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,render
from .models import Order, OrderItem
from cart.carts import Cart
from product.models import Product
from django.http import HttpResponse


class OrderCheckout(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'order/checkout.html'
    fields = ['first_name', 'last_name', 'email', 'address', 'city', 'zip_code']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
    
    def form_valid(self, form):
        cart = Cart(self.request)
        if not cart:
            return redirect('cart')
            
        order = form.save(commit=False)
        order.user = self.request.user
        order.total = cart.get_total_price()
        order.payment_method = self.request.POST.get('payment_method', 'cod')
        
        # Set paid status based on payment method
        if order.payment_method == 'cod':
            order.paid = False
        
        order.save()
        
        # Create order items
        for item in cart:
            product = Product.objects.get(id=item['product']['id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                price=item['price'],
                quantity=item['quantity']
            )
            
        # Clear the cart
        cart.clear()
        
        return redirect('order-success')
    
    def order_success(request):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Order Success</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-md-8">
                        <div class="card">
                            <div class="card-body text-center">
                                <h1 class="card-title text-success">Order Successful!</h1>
                                <p class="card-text">Thank you for your order. We'll process it soon.</p>
                                <a href="/" class="btn btn-primary">Return to Home</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html_content)

