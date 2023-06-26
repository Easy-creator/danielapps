from django.shortcuts import render
from rest_framework import generics
from products.models import Products as Post
from .apis import PostApi
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAuthenticated
from rest_framework.permissions import IsAuthenticated


class PostUserWrPermission(BasePermission):
    message = "You can only edit this post if you are the user"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

#class PostList(generics.ListAPIView):
class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostApi

#class PostDetails(generics.RetrieveDestroyAPIView):
class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostUserWrPermission):
    permission_classes = [PostUserWrPermission]
    queryset = Post.objects.all()
    serializer_class = PostApi

# admin logins = 'eze@eze.com', '1'