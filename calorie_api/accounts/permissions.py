from rest_framework.permissions import BasePermission


class IsManagerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ["manager", "admin"]:
            return True
        return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return request.user.is_authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
