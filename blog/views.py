from django.shortcuts import render
from blog.serializer import PostSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import BlogPost

# Create your views here.
class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()