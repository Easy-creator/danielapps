from rest_framework import serializers
from blog.models import BlogPost, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer() 

    class Meta:
        model = BlogPost
        fields = ('title', 'category', 'date', 'post', 'updated')

