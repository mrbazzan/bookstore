
from django.urls import path, include
from .views import BookViewSet


urlpatterns = [
    path('books/', BookViewSet.as_view({
        'get': "list",
        'post': "create",
    })),
    path('books/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }))
]
