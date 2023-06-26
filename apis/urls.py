from django.urls import path
from django.views.generic import TemplateView
from .views import PostList, PostDetails

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetails.as_view(), name="detailcreate"),
    path('', PostList.as_view(), name="listcreate")
]