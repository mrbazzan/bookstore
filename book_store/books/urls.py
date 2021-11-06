
from django.urls import path, include
from .views import BookViewSet


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('books/', BookViewSet.as_view({
        'get': "list",
        'post': "create",
    })),
    path('books/<str:pk>', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))
]
