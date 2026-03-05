from rest_framework.permissions import BasePermission

from .models import User


class IsStudent(BasePermission):
    def has_permission(self, request, view) -> bool:
        user: User = request.user
        return bool(user and user.is_authenticated and user.is_student())


class IsHostelAdmin(BasePermission):
    def has_permission(self, request, view) -> bool:
        user: User = request.user
        return bool(user and user.is_authenticated and user.is_hostel_admin())


class IsFinanceOfficer(BasePermission):
    def has_permission(self, request, view) -> bool:
        user: User = request.user
        return bool(user and user.is_authenticated and user.is_finance_officer())


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view) -> bool:
        user: User = request.user
        return bool(user and user.is_authenticated and user.is_super_admin())

