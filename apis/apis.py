from rest_framework import serializers
from products.models import Products, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostApi(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Products
        #fields = '__all__'
        fields = ('name', 'price', 'image', 'category', 'date', )