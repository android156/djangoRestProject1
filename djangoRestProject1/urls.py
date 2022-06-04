"""djangoRestProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from messageapp.views import MessageModelViewSet
from todoapp.views import ToDoModelViewSet, ProjectModelViewSet, MyApiView, ProjectLimitOffsetPaginationViewSet
from userapp.views import AppUserModelViewSet, start_page, AppUserListUpdateViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('users', AppUserListUpdateViewSet)
router.register('projects', ProjectLimitOffsetPaginationViewSet)
router.register('todo', ToDoModelViewSet)
router.register('messages', MessageModelViewSet)
# router.register('users-for-react', AppUserModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', start_page, name='main'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-view/', MyApiView.as_view(), name='api-view'),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/messages-v/1.0', include('messageapp.urls', namespace='1.0')),  # NamespaceVersioning
    path('api/messages-v/2.0', include('messageapp.urls', namespace='2.0')),  # NamespaceVersioning


    path('graphql/', GraphQLView.as_view(graphiql=True)),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',  # шаблон через регулярку
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    # шаблон через регулярку
    re_path(r'^api/(?P<version>\d\.\d)/messages-v/$', MessageModelViewSet.as_view({'get': 'list'}))  # URLPathVersioning

]
