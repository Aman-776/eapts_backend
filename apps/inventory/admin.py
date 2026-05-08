from django.contrib import admin
from .models import (
    DrugCategory,
    PrescriptionStatus,
    TransferRequestStatus,
    PaymentMethod,
    Drug,
    DrugAttributeType,
    DrugAttribute,
    Stock,
    StockTransferRequest,
    TransferItem,
    Dispensing,
    DispensingItem,
    Prescription,
    PrescriptionItem,
)

# -------------------------------
# Metadata Tables
# -------------------------------
admin.site.register(DrugCategory)
admin.site.register(PrescriptionStatus)
admin.site.register(TransferRequestStatus)
admin.site.register(PaymentMethod)

# -------------------------------
# Drug & Drug Attributes
# -------------------------------
admin.site.register(Drug)
admin.site.register(DrugAttributeType)
admin.site.register(DrugAttribute)

# -------------------------------
# Stock & Transfer
# -------------------------------
admin.site.register(Stock)
admin.site.register(StockTransferRequest)
admin.site.register(TransferItem)

# -------------------------------
# Dispensing & Prescription
# -------------------------------
admin.site.register(Dispensing)
admin.site.register(DispensingItem)
admin.site.register(Prescription)
admin.site.register(PrescriptionItem)
