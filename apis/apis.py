<<<<<<< HEAD
from rest_framework import serializers
from products.models import Products

class PostApi(serializers.ModelSerializer):
    class Meta:
        model = Products
        #fields = '__all__'
=======
from rest_framework import serializers
from products.models import Products

class PostApi(serializers.ModelSerializer):
    class Meta:
        model = Products
        #fields = '__all__'
>>>>>>> ebe7595 (main)
        fields = ('name', 'price', 'image', 'category', 'date', )