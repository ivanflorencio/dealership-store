from django.contrib import admin

# Register your models here.
from .models import Category, Product, Costumer, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Costumer)
admin.site.register(Order)