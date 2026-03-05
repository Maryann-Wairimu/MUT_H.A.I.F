from rest_framework import permissions, viewsets

from accounts.permissions import IsFinanceOfficer, IsSuperAdmin
from .models import FeeType, HostelFeeStructure, Invoice, Payment
from .serializers import (
    FeeTypeSerializer,
    HostelFeeStructureSerializer,
    InvoiceSerializer,
    PaymentSerializer,
)


class FeeTypeViewSet(viewsets.ModelViewSet):
    queryset = FeeType.objects.all().order_by("name")
    serializer_class = FeeTypeSerializer
    permission_classes = [IsFinanceOfficer | IsSuperAdmin]


class HostelFeeStructureViewSet(viewsets.ModelViewSet):
    queryset = HostelFeeStructure.objects.select_related(
        "hostel", "room_type", "fee_type"
    )
    serializer_class = HostelFeeStructureSerializer
    permission_classes = [IsFinanceOfficer | IsSuperAdmin]


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related("student", "allocation")
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated & (IsFinanceOfficer | IsSuperAdmin)]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related("invoice")
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated & (IsFinanceOfficer | IsSuperAdmin)]
