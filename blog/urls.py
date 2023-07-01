from blog.views import PostList, PostUpdate, PostUpdateDelete
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    # path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:id>/', PostUpdate.as_view(), name='post_update'),
    path('update/<int:id>/', PostUpdateDelete.as_view(), name='post_update_delete'),
]
