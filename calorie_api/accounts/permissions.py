from rest_framework import permissions


class IsManagerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['manager', 'admin']:
            return True
        return False 
