from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .models import Category, Product, Slider
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
            'featured_products': Product.objects.filter(featured=True),
            'sliders': Slider.objects.all()
        })
        return context
    
class ProductDetailView(TemplateView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'product/product-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(slug=self.kwargs['slug'])
        context.update({
            'product': product,
            'related_products': product.related
        })
        return context

class CategoryDetailView(TemplateView):
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'product/category-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category': Category.objects.get(slug=self.kwargs['slug'])
        })
        return context

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        if not request.session.get('cart'):
            request.session['cart'] = {}
        
        cart = request.session['cart']
        product_id_str = str(product_id)
        
        if product_id_str in cart:
            cart[product_id_str] += 1
        else:
            cart[product_id_str] = 1
        
        request.session.modified = True
        messages.success(request, f'{product.title} added to cart')
        
        return redirect('product-detail', slug=product.slug)
    return redirect('home')

class ProductListView(ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = Product.objects.all()
        sort_by = self.request.GET.get('sort')
        
        if sort_by == 'price':
            queryset = queryset.order_by('price')
        elif sort_by == 'newest':
            queryset = queryset.order_by('-created')
        elif sort_by == 'orders':
            queryset = queryset.order_by('-rating_count')
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort', '')
        return context
