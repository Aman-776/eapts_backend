# inventory/models.py
from django.db import models
from apps.person.models import Patient

# -------------------------------
# Metadata Tables
# -------------------------------
class DrugCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class PrescriptionStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TransferRequestStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------------------
# Drug & Drug Attributes
# -------------------------------
class Drug(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(DrugCategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class DrugAttributeType(models.Model):
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)  # e.g., 'string', 'integer', 'date'

    def __str__(self):
        return self.name


class DrugAttribute(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name="attributes")
    attribute_type = models.ForeignKey(DrugAttributeType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.drug.name} - {self.attribute_type.name}"


# -------------------------------
# Stock & Transfer
# -------------------------------
class Stock(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name="stocks")
    location = models.ForeignKey("locations.Location", on_delete=models.CASCADE, related_name="stocks")
    batch_number = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiry_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.drug.name} @ {self.location.name}"


class StockTransferRequest(models.Model):
    from_location = models.ForeignKey("locations.Location", on_delete=models.CASCADE, related_name="transfer_requests_sent")
    to_location = models.ForeignKey("locations.Location", on_delete=models.CASCADE, related_name="transfer_requests_received")
    status = models.ForeignKey(TransferRequestStatus, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Transfer {self.id}: {self.from_location} -> {self.to_location}"


class TransferItem(models.Model):
    request = models.ForeignKey(StockTransferRequest, on_delete=models.CASCADE, related_name="items")
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    batch_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} x {self.drug.name}"


# -------------------------------
# Dispensing & Prescription
# -------------------------------
class Dispensing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="dispensings")
    location = models.ForeignKey("locations.Location", on_delete=models.CASCADE, related_name="dispensings")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Dispensing #{self.id} for {self.patient}"


class DispensingItem(models.Model):
    dispensing = models.ForeignKey(Dispensing, on_delete=models.CASCADE, related_name="items")
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    batch_number = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.drug.name}"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="prescriptions")
    doctor_name = models.CharField(max_length=200)
    status = models.ForeignKey(PrescriptionStatus, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.id} for {self.patient}"


class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="items")
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} x {self.drug.name}"