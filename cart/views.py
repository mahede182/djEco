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
        
        return redirect('product-detail', slug=product.slug)
