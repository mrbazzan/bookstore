
from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class CustomPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not isinstance(request.user, AnonymousUser) and request.user.is_admin:
            return True

        return request.user == obj
