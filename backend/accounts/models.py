from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = "student", "Student"
        HOSTEL_ADMIN = "hostel_admin", "Hostel Admin"
        FINANCE_OFFICER = "finance_officer", "Finance Officer"
        SUPER_ADMIN = "super_admin", "Super Admin"

    role = models.CharField(
        max_length=32,
        choices=Roles.choices,
        default=Roles.STUDENT,
    )

    def is_student(self) -> bool:
        return self.role == self.Roles.STUDENT

    def is_hostel_admin(self) -> bool:
        return self.role == self.Roles.HOSTEL_ADMIN

    def is_finance_officer(self) -> bool:
        return self.role == self.Roles.FINANCE_OFFICER

    def is_super_admin(self) -> bool:
        return self.role == self.Roles.SUPER_ADMIN
