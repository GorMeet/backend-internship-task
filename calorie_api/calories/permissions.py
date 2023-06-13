from rest_framework.permissions import BasePermission, IsAuthenticated

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
