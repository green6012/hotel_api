from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Cho phép phương thức GET, HEAD, OPTIONS bất kể người dùng là ai
        if request.method in permissions.SAFE_METHODS:
            return True

        # Kiểm tra xem người dùng có phải là chủ sở hữu của object hay không
        return obj.created_by == request.user