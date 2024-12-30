from django.shortcuts import render
from django.views.generic import TemplateView
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