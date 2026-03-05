from django.db import models


class ReportSnapshot(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    # Simple JSON field to store aggregated data; can be refined later
    data = models.JSONField()

    def __str__(self) -> str:
        return f"{self.name} @ {self.created_at:%Y-%m-%d}"
