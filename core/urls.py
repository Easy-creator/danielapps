
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls', namespace='blog_api')),
    path('apiauth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/api/', include('users.urls', namespace='users')),

    # token refresh for auth api
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]