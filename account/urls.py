
from django.urls import path
from account.views import UserView, UserDetail

urlpatterns = [
    path('users/', UserView.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
]
