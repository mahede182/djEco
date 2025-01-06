from django.urls import path
from .views import HomeView, ProductDetailView, add_to_cart, CategoryDetailView, ProductListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]