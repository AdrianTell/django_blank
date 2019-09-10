from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework import permissions
from hashblank.blankapp import views

from rest_framework_simplejwt import views as jwt_views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_info = openapi.Info(
    title="Blank API",
    default_version='v1',
    description="template django project"
)

SchemaView = get_schema_view(
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# urlpatterns required for settings values
required_urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #path('api/v1/token/', jwt_views.TokenObtainPairView.as_view()),
    #path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('api/v1/token/', views.CustomTokenObtainView.as_view()),
]

urlpatterns = [
    
] + required_urlpatterns