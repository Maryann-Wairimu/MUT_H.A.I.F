from rest_framework import serializers

from .models import Program, Student


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ["id", "code", "name"]


class StudentSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source="user.get_full_name", read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "registration_number",
            "user",
            "user_full_name",
            "program",
            "year_of_study",
            "campus",
            "is_hostel_eligible",
        ]

