from django.core.management.base import BaseCommand
from product.models import Category, Product, Slider
import requests
from django.utils.text import slugify
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Creating data...")
        response = requests.get('https://fakestoreapi.com/products')
        products = response.json()
        
        # Track categories we've already created
        categories = {}
        
        for product_data in products:
            category_title = product_data['category']
            
            # Create category if it doesn't exist
            if category_title not in categories:
                categories[category_title] = Category.objects.create(
                    title=category_title,
                    slug=slugify(category_title)
                )
            
            # Create product using existing category
            Product.objects.create(
                title=product_data['title'],
                slug=slugify(product_data['title']),
                thumbnail=product_data['image'],
                price=product_data['price'],
                description=product_data['description'],
                category=categories[category_title],
                rating_rate=product_data['rating']['rate'],
                rating_count=product_data['rating']['count']
            )
            
        print("Data created successfully")