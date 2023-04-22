from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == "GET"
