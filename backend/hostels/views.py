from rest_framework import permissions, viewsets

from accounts.permissions import IsHostelAdmin, IsStudent
from .models import Allocation, Hostel, Room
from .serializers import AllocationSerializer, HostelSerializer, RoomSerializer


class HostelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hostel.objects.all().order_by("name")
    serializer_class = HostelSerializer
    permission_classes = [permissions.AllowAny]


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.select_related("hostel", "room_type").all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]


class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.select_related("student", "room").all()
    serializer_class = AllocationSerializer
    permission_classes = [permissions.IsAuthenticated & (IsStudent | IsHostelAdmin)]
