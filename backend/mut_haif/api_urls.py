from django.urls import include, path
from rest_framework.routers import DefaultRouter

from accounts.views import LoginView, LogoutView, MeView
from finance.views import (
    FeeTypeViewSet,
    HostelFeeStructureViewSet,
    InvoiceViewSet,
    PaymentViewSet,
)
from hostels.views import AllocationViewSet, HostelViewSet, RoomViewSet
from reports.views import ReportSnapshotViewSet
from students.views import ProgramViewSet, StudentViewSet

router = DefaultRouter()
router.register("programs", ProgramViewSet, basename="program")
router.register("students", StudentViewSet, basename="student")
router.register("hostels", HostelViewSet, basename="hostel")
router.register("rooms", RoomViewSet, basename="room")
router.register("allocations", AllocationViewSet, basename="allocation")
router.register("fee-types", FeeTypeViewSet, basename="fee-type")
router.register("hostel-fees", HostelFeeStructureViewSet, basename="hostel-fee")
router.register("invoices", InvoiceViewSet, basename="invoice")
router.register("payments", PaymentViewSet, basename="payment")
router.register("report-snapshots", ReportSnapshotViewSet, basename="report-snapshot")


urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/me/", MeView.as_view(), name="me"),
    path("", include(router.urls)),
]

