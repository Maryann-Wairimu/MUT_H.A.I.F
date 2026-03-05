from django.conf import settings
from django.db import models


class Hostel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    campus = models.CharField(max_length=128, blank=True)
    gender = models.CharField(
        max_length=16,
        choices=(
            ("male", "Male"),
            ("female", "Female"),
            ("mixed", "Mixed"),
        ),
        default="mixed",
    )

    def __str__(self) -> str:
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("name", "capacity")

    def __str__(self) -> str:
        return f"{self.name} ({self.capacity})"


class Room(models.Model):
    hostel = models.ForeignKey(
        Hostel,
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    number = models.CharField(max_length=32)
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.PROTECT,
        related_name="rooms",
    )

    class Meta:
        unique_together = ("hostel", "number")

    def __str__(self) -> str:
        return f"{self.hostel.name} {self.number}"


class Allocation(models.Model):
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="allocations",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="allocations",
    )
    allocated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="room_allocations_made",
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "room", "is_active"],
                condition=models.Q(is_active=True),
                name="unique_active_allocation_per_room_and_student",
            )
        ]

    def __str__(self) -> str:
        return f"{self.student} -> {self.room}"
