from rest_framework import permissions, viewsets

from .models import Program, Student
from .serializers import ProgramSerializer, StudentSerializer


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all().order_by("code")
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("user", "program").all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
