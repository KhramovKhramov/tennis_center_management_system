"""URL configuration for app."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

api_urlpatterns = [
    path('users/', include('apps.users.urls'), name='users'),
    path(settings.SCHEMA_URL, SpectacularAPIView.as_view(), name='schema'),
    path(
        settings.SWAGGER_URL,
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger',
    ),
    path(
        settings.REDOC_URL,
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]
