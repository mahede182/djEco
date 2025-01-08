from django.views.generic import TemplateView
from .carts import Cart
from product.models import Product
from django.shortcuts import get_object_or_404, redirect
class AddToCart(TemplateView):
    def post(self, request, *args, **kwargs):
        product_id = kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        cart = Cart(request)
        cart.update(product_id, quantity=quantity)
        
        return redirect('cart')

class CartItems(TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        
        product_id = request.GET.get('product_id')
        quantity = request.GET.get('quantity')
        clear = request.GET.get('clear')
        
        if product_id and quantity:
            try:
                quantity = int(quantity)
                cart.update(product_id, quantity=quantity)
            except ValueError:
                # Handle invalid quantity value
                pass
            return redirect('cart')
            
        if clear:
            cart.clear()
            return redirect('cart')
            
        return super().get(request, *args, **kwargs)
    