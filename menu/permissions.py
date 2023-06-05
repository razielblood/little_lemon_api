from rest_framework import permissions
from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView


class CategoryPermissions(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view: GenericAPIView):
        user = request.user
        method = request.method

        PERMISSION_FUNCTION = {
            "GET": self.get_permissions,
            "POST": self.post_permissions,
            "PUT": self.put_permissions,
            "PATCH": self.patch_permissions,
            "DELETE": self.delete_permissions,
        }
        permission_function = PERMISSION_FUNCTION.get(method)
        if not permission_function:
            return False
        return permission_function(user, view)

    def get_permissions(self, user: User, view: GenericAPIView) -> bool:
        return True

    def post_permissions(self, user: User, view: GenericAPIView) -> bool:
        if user.is_superuser or user.groups.filter(name="Manager").exists():
            return True
        return False

    def put_permissions(self, user: User, view: GenericAPIView) -> bool:
        return self.post_permissions(user, view)

    def patch_permissions(self, user: User, view: GenericAPIView) -> bool:
        return self.post_permissions(user, view)

    def delete_permissions(self, user: User, view: GenericAPIView) -> bool:
        return self.post_permissions(user, view)


class MenuItemPermissions(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, view: GenericAPIView):
        user = request.user
        method = request.method

        PERMISSION_FUNCTION = {
            "GET": self.get_permissions,
            "POST": self.post_permissions,
            "PUT": self.put_permissions,
            "PATCH": self.patch_permissions,
            "DELETE": self.delete_permissions,
        }
        permission_function = PERMISSION_FUNCTION.get(method)
        if not permission_function:
            return False
        return permission_function(user, view)

    def get_permissions(self, user: User, view: GenericAPIView) -> bool:
        return True

    def post_permissions(self, user: User, view: GenericAPIView) -> bool:
        if user.is_superuser or user.groups.filter(name="Manager").exists():
            return True
        return False

    def put_permissions(self, user: User, view: GenericAPIView) -> bool:
        return self.post_permissions(user, view)

    def patch_permissions(self, user: User, view: GenericAPIView) -> bool:
        return self.post_permissions(user, view)

    def delete_permissions(self, user: User, view: GenericAPIView) -> bool:
        return self.post_permissions(user, view)
