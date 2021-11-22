from store.models import Product, Category
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'description', 'price', 'image', 'featured']


