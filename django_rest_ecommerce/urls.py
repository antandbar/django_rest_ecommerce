from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, logout, UserToken

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de PI",
      default_version='v0.1',
      description="Documentación pública de Api de Ecomerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="antonio@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('logout/', logout.as_view(), name = 'logout'),
    path('',Login.as_view(), name = 'login'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh_token'),
    path('usuario/', include('apps.users.api.urls')),
    #path('products/', include('apps.products.api.urls')),
    path('products/', include('apps.products.api.routers')),
]
