from rest_framework import permissions, viewsets

from .models import ReportSnapshot
from .serializers import ReportSnapshotSerializer


class ReportSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReportSnapshot.objects.all().order_by("-created_at")
    serializer_class = ReportSnapshotSerializer
    permission_classes = [permissions.IsAdminUser]
