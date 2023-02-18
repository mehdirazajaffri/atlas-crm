from django.db import models

from core.models import BaseModel


class Project(BaseModel):
    PROJECT_TYPES_CHOICES = (
        ("pilling", "Pilling"),
        ("excavation", "Excavation"),
        ("foundation", "Foundation"),
        ("dewatering", "Dewatering"),
        ("shoring", "Shoring"),
        ("concrete", "Concrete"),
    )

    STATUS_CHOICES = (
        ("signed", "Signed"),
        ("running", "Running"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("onhold", "On Hold"),
    )
    project_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    type = models.CharField(max_length=50, choices=PROJECT_TYPES_CHOICES)
    name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    initial_contract_amount = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    variation = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    delay_penalty = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    final_contract_amount = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    placement_terms = models.TextField(blank=True, null=True)
    agreement_sign_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.project_id) + " - " + self.name


class Invoice(BaseModel):
    INVOICE_STATUS = (
        ("paid", "Paid"),
        ("unpaid", "Unpaid"),
        ("partially_paid", "Partially Paid"),
    )
    INVOICE_TYPE_CHOICES = (
        ("advance", "Advance"),
        ("running", "Running"),
        ("final_bill", "Final Bill"),
    )
    invoice_no = models.CharField(max_length=100, blank=True, null=True, unique=True)
    project = models.ForeignKey(Project, related_name="invoices", on_delete=models.CASCADE)
    invoice_type = models.CharField(max_length=50, choices=INVOICE_TYPE_CHOICES)
    invoice_date = models.DateField()
    due_date = models.DateField()
    total_work_done = models.CharField(max_length=200)
    previous_work_done = models.CharField(max_length=200)
    current_work_done = models.CharField(max_length=200)
    balance_work_done = models.CharField(max_length=200)
    advance = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    retention = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    material = models.CharField(max_length=200)
    net_invoice_amount = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    vat = models.DecimalField(max_digits=100, decimal_places=0, blank=True, null=True)
    due_invoice_amount = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    status = models.CharField(max_length=50, choices=INVOICE_STATUS)
    void = models.BooleanField("Void", default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.invoice_no, self.project.name)


class Payment(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=100, decimal_places=0, blank=True, null=True
    )
    cheque_no = models.CharField(max_length=50)
    cheque_received_date = models.DateField()
    cheque_date = models.DateField(verbose_name="Cheque Clearing Due Date")
    bank_name = models.CharField(max_length=100)
    cash = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    payment_proof = models.FileField(upload_to="payment_proofs", blank=True, null=True, verbose_name="Payment Proof")
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
                self.invoice.invoice_no
                + " - "
                + self.invoice.project.name
        )
