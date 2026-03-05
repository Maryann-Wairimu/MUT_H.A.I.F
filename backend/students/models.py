from django.conf import settings
from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    registration_number = models.CharField(max_length=64, unique=True)
    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT,
        related_name="students",
    )
    year_of_study = models.PositiveSmallIntegerField()
    campus = models.CharField(max_length=128, blank=True)
    is_hostel_eligible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.registration_number} - {self.user.get_full_name()}"
