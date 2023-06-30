from django.shortcuts import render
from blog.serializer import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import BlogPost

# Create your views here.
class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()

class PostUpdate(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_queryset(self):
        return BlogPost.objects.all()
    
class PostUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_queryset(self):
        return BlogPost.objects.all()