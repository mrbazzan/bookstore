from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class KidCanOnlyViewUnder18Books(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_kid:
            return obj.pg == request.user.age

        return True
