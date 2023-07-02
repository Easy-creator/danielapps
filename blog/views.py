from django.shortcuts import render
from blog.serializer import PostSerializer, PostCreateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import BlogPost

# Create your views here.
class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()
    
# to create a post
class PostCreate(CreateAPIView):
    permission_classes = []
    serializer_class = PostCreateSerializer

# only retrieves a Post
class PostUpdate(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_queryset(self):
        return BlogPost.objects.all()

# retrieve, Update and Deletes a post    
class PostUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_queryset(self):
        return BlogPost.objects.all()