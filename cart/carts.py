from django.conf import settings
from product.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart_id = settings.CART_ID
        cart = self.session.get(self.cart_id)
        self.cart = self.session[self.cart_id] = cart if cart else {}
    
    def __str__(self):
        return str(self.cart)
    
    def update(self, product_id, quantity):
        product = Product.objects.get(id=product_id)
        self.session[self.cart_id].setdefault(product_id, {'quantity': 0, 'price': float(product.price)})
        update_quantity = quantity
        self.session[self.cart_id][product_id]['quantity'] = update_quantity
        self.session[self.cart_id][product_id]['subtotal'] = float(product.price) * update_quantity
        if update_quantity < 1:
            del self.session[self.cart_id][product_id]
        self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = {
                "id": product.id,
                "title": product.title,
                "category": product.category.title,
                "price": float(product.price),
                "thumbnail": product.thumbnail,
                "slug": product.slug,
            }
            cart[str(product.id)]['subtotal'] = float(product.price) * cart[str(product.id)]['quantity']
            yield cart[str(product.id)]
    
    def save(self):
        self.session.modified = True
        
    def __len__(self):
        return len(list(self.cart.keys()))
    
    def clear(self):
        try:
            del self.session[self.cart_id]
            self.save()
        except KeyError:
            pass
