from rest_framework import serializers

from .models import Allocation, Hostel, Room, RoomType


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ["id", "name", "campus", "gender"]


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ["id", "name", "capacity"]


class RoomSerializer(serializers.ModelSerializer):
    hostel = HostelSerializer(read_only=True)
    room_type = RoomTypeSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ["id", "hostel", "number", "room_type"]


class AllocationSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Allocation
        fields = [
            "id",
            "student",
            "room",
            "allocated_by",
            "start_date",
            "end_date",
            "is_active",
            "created_at",
        ]

