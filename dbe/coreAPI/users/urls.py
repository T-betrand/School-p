from django.urls import path 

from .views import UserViewSet, ServiceProviderViewSet, SkillsViewSet, JobsViewSet

urlpatterns = [

    path('users', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('users/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    path('service_providers', ServiceProviderViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('service_providers/<str:pk>', ServiceProviderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    path('skills', SkillsViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('skill/<str:pk>', SkillsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

    path('jobs', JobsViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('job/<str:pk>', JobsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),

]