from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponseRedirect


schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version='v1',
        description="API documentation for the Portfolio project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xurshidbekyunusaliyev2@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/projects/')),  
    path('', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
