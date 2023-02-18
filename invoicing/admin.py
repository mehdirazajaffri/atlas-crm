from django.contrib import admin

from core.admin import BaseAdmin
from invoicing.models import Payment, Project, Invoice


class InvoiceInline(admin.StackedInline):
    model = Invoice
    extra = 0


@admin.register(Project)
class ProjectAdmin(BaseAdmin):
    inlines = [InvoiceInline, ]
    list_display = (
        "project_id",
        "type",
        "name",
        "client_name",
        "location",
        "initial_contract_amount",
        "created_at"
    )
    list_filter = ("status", "location", "country",)
    search_fields = (
        "name",
        "id",
        "client_name",
        "description"
    )


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(BaseAdmin):
    inlines = [PaymentInline, ]
    search_fields = ("id", "project__id", "project__name",)
    list_display = (
        ("invoice_no", "invoice_type", "project", "invoice_date",
         "status", "due_invoice_amount",)
    )
    list_filter = ("status", "void", "invoice_type", "project__project_id",)

    class Media:
        js = ('js/invoice.js',)


@admin.register(Payment)
class PaymentAdmin(BaseAdmin):
    search_fields = ("invoice__invoice_no", "invoice__project__project_id", "invoice__project__name",)
    list_display = (
        ("project_id", "invoice", "amount", "cheque_received_date", "bank_name", "cash")
    )
    list_filter = ("invoice__status", "invoice__project__name",
                   "invoice__project__client_name", "invoice__project__location", "cheque_date",)

    def project_id(self, obj):
        return obj.invoice.project.project_id or None
