from rest_framework.permissions import BasePermission


class SuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and (request.user.user_type == 1))


class HrUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and (request.user.user_type == 2))


class NormalUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and (request.user.user_type == 3))
