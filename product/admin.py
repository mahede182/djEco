from django.contrib import admin

# Register your models here.
from .models import Category, Product, Slider

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin) 
admin.site.register(Slider)

