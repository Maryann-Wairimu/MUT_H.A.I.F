from rest_framework import serializers

from .models import FeeType, HostelFeeStructure, Invoice, Payment


class FeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeType
        fields = ["id", "name", "description"]


class HostelFeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelFeeStructure
        fields = [
            "id",
            "hostel",
            "room_type",
            "fee_type",
            "amount",
            "academic_year",
        ]


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            "id",
            "student",
            "allocation",
            "total_amount",
            "balance",
            "created_at",
            "due_date",
            "is_settled",
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "invoice",
            "amount",
            "method",
            "reference",
            "paid_at",
            "recorded_by",
        ]

