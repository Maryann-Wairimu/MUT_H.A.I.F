from django.conf import settings
from django.db import models


class FeeType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class HostelFeeStructure(models.Model):
    hostel = models.ForeignKey(
        "hostels.Hostel",
        on_delete=models.CASCADE,
        related_name="fee_structures",
    )
    room_type = models.ForeignKey(
        "hostels.RoomType",
        on_delete=models.CASCADE,
        related_name="fee_structures",
    )
    fee_type = models.ForeignKey(
        FeeType,
        on_delete=models.CASCADE,
        related_name="hostel_fees",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.CharField(max_length=9, help_text="e.g. 2025/2026")

    class Meta:
        unique_together = ("hostel", "room_type", "fee_type", "academic_year")

    def __str__(self) -> str:
        return f"{self.hostel} - {self.room_type} - {self.fee_type} ({self.academic_year})"


class Invoice(models.Model):
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="invoices",
    )
    allocation = models.ForeignKey(
        "hostels.Allocation",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="invoices",
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    is_settled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Invoice {self.id} - {self.student}"


class Payment(models.Model):
    class Methods(models.TextChoices):
        CASH = "cash", "Cash"
        BANK = "bank", "Bank"
        MOBILE = "mobile", "Mobile Money"
        OTHER = "other", "Other"

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="payments",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(
        max_length=16,
        choices=Methods.choices,
        default=Methods.CASH,
    )
    reference = models.CharField(max_length=128, blank=True)
    paid_at = models.DateTimeField(auto_now_add=True)
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments_recorded",
    )

    def __str__(self) -> str:
        return f"Payment {self.amount} for {self.invoice}"
