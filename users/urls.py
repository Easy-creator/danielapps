from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView
from rest_framework.authtoken.views import obtain_auth_token
from . import views
app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    #path('login/', obtain_auth_token, name='login'),
    #path('logout/', views.logout_user, name='logout')
]
