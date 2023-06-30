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





# class PostSerializer(serializers.ModelSerializer):
#     category = serializers.CharField(source='category.name')

#     class Meta:
#         model = Post
#         fields = ['title', 'category', 'date', 'post', 'updated']

#     def create(self, validated_data):
#         category_data = validated_data.pop('category', None)
#         if category_data:
#             category_name = category_data['name']
#             category, _ = Category.objects.get_or_create(name=category_name)
#             validated_data['category'] = category
#         return super().create(validated_data)

# class PostSerializer(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(read_only=True)

#     class Meta:
#         model = Post
#         fields = ['title', 'category', 'date', 'post', 'updated']
