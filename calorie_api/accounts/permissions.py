from rest_framework.permissions import BasePermission


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['manager', 'admin']:
            return True
        return False 
