from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ACCREATOR DOCS",
        default_version='v1',
        description="Account creation web-service for modern world",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="stanichgame@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/users/', include('user.urls')),
    path('api/mails/', include('mail.urls')),

    path('admin/', admin.site.urls),
    path(r'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
