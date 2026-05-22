# permissions.py

from rest_framework.permissions import BasePermission

class IsAdminUserType(BasePermission):

    def has_permission(self, request, view):

        # USER LOGIN CHECK
        if not request.user or not request.user.is_authenticated:
            return False

        # USER TYPE CHECK
        if request.user.user_type.user_type == "Admin":
            return True

        return False