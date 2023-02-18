# Generated by Django 4.0.3 on 2023-02-18 10:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('invoice_type', models.CharField(choices=[('advance', 'Advance'), ('running', 'Running'), ('final_bill', 'Final Bill')], max_length=50)),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('total_work_done', models.CharField(max_length=200)),
                ('previous_work_done', models.CharField(max_length=200)),
                ('current_work_done', models.CharField(max_length=200)),
                ('balance_work_done', models.CharField(max_length=200)),
                ('advance', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('retention', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('material', models.CharField(max_length=200)),
                ('net_invoice_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('vat', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('due_invoice_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid'), ('partially_paid', 'Partially Paid')], max_length=50)),
                ('void', models.BooleanField(default=False, verbose_name='Void')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('pilling', 'Pilling'), ('excavation', 'Excavation'), ('foundation', 'Foundation'), ('dewatering', 'Dewatering'), ('shoring', 'Shoring'), ('concrete', 'Concrete')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('signed', 'Signed'), ('running', 'Running'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('onhold', 'On Hold')], max_length=50)),
                ('initial_contract_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('variation', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('delay_penalty', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('final_contract_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('placement_terms', models.TextField(blank=True, null=True)),
                ('agreement_sign_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True)),
                ('cheque_no', models.CharField(max_length=50)),
                ('cheque_received_date', models.DateField()),
                ('cheque_date', models.DateField(verbose_name='Cheque Clearing Due Date')),
                ('bank_name', models.CharField(max_length=100)),
                ('cash', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('payment_proof', models.FileField(blank=True, null=True, upload_to='payment_proofs', verbose_name='Payment Proof')),
                ('remarks', models.TextField(blank=True, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicing.invoice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='invoicing.project'),
        ),
    ]
