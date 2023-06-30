from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls', namespace='apis')),
    path('apiauth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/api/', include('users.urls', namespace='users')),
    path('blog/api/', include('blog.urls', namespace='blog')),
]

if settings.DEBUG or not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)