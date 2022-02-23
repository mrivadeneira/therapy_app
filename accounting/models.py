from email.policy import default
from django.db import models
from patients.models import PatientSessions
from therapists.models import Therapists

class Partners(models.Model):
    id_document_cust = models.IntegerField(primary_key=False, unique=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    class PartnersPositions(models.IntegerChoices):
        THERAPIST = 1
        CAPITALIST = 2
    position = models.IntegerField(choices=PartnersPositions.choices)
    created_at = models.DateTimeField(auto_now_add=True)


class CapitalContributions(models.Model):
    partner = models.ForeignKey(
        Partners,
        on_delete = models.SET('DELETED'),
        related_name = 'partner_contributions',
    )
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class CapitalWithdrawals(models.Model):
    partner = models.ForeignKey(
        Partners,
        on_delete = models.SET('DELETED'),
        related_name = 'partner_withdrawals',
    )
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Clients(models.Model):
    id_document_cust = models.IntegerField()
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class PaymentMethods(models.Model):
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Rentals(models.Model):
    client = models.ForeignKey(
        Clients,
        on_delete = models.SET('DELETED'),
        related_name = 'client_rental',
    )
    class Module(models.IntegerChoices):
        MORNING = 1
        AFTERNOON = 2
    module = models.IntegerField(choices = Module.choices)
    period_from = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Bills(models.Model):
    client = models.ForeignKey(
        Clients,
        on_delete = models.SET('DELETED'),
        db_column = 'id_document_cust',
    )
    pmt_method = models.ForeignKey(
        PaymentMethods,
        on_delete = models.SET('DELETED'),
    )
    is_rental = models.BooleanField(default=False)
    rental = models.ForeignKey(
        Rentals,
        on_delete = models.SET('DELETED'),
        related_name = 'rental_bill',
        null = True,
    )
    is_session = models.BooleanField(default=False)
    session = models.ForeignKey(
        PatientSessions,
        on_delete = models.SET('DELETED'),
        related_name = 'session_bill',
        null = True,
    )
    date = models.DateField()
    class BillingOperations(models.IntegerChoices):
        RENTAL = 1
        SESSIONS = 2
    operation_type = models.IntegerField(choices=BillingOperations.choices)
    units = models.SmallIntegerField()
    unit_price = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class CreditNotes(models.Model):
    bill = models.ForeignKey(
        Bills,
        on_delete = models.SET('DELETED'),
        related_name = 'bill_creditnote',
    )
    reason = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Providers(models.Model):
    tax_identificator = models.IntegerField()
    identificator = models.IntegerField()
    is_company = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProviderDetails(models.Model):
    provider = models.ForeignKey(
        Providers,
        on_delete = models.CASCADE,
        related_name = 'provider_details',
    )
    cbu = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    mobile_1 = models.PositiveBigIntegerField()
    mobile_2 = models.PositiveBigIntegerField(null=True)
    zip_code = models.SmallIntegerField()
    address_street = models.CharField(max_length=200)
    address_num = models.IntegerField()
    address_floor = models.CharField(max_length=10, null=True)
    address_ap = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProviderServices(models.Model):
    provider = models.ForeignKey(
        Providers,
        on_delete = models.CASCADE,
        related_name = 'provider_services',
    )
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class PurchaseInvoices(models.Model):
    provider = models.ForeignKey(
        Providers,
        on_delete = models.SET('DELETED'),
        related_name = 'provider_purchase',
    )
    concept = models.ForeignKey(
        ProviderServices,
        on_delete = models.SET('DELETED'),
    )
    to_company = models.BooleanField(default=False)
    company_id = models.IntegerField(null=True)
    to_therapist = models.BooleanField(default=False)
    therapist_id = models.ForeignKey(
        Therapists,
        on_delete = models.SET('DELETED'),
        null = True,
    )
    units = models.SmallIntegerField()
    unit_price = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Assets(models.Model):
    purchase = models.ForeignKey(
        PurchaseInvoices,
        on_delete = models.SET('DELETED'),
        related_name = 'purchase_asset'
    )
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class MoneyInReceipts(models.Model):
    is_bill = models.BooleanField(default=False)
    bill = models.ForeignKey(
        Bills,
        on_delete = models.SET('DELETED'),
        related_name = 'bill_moneyin',
        null = True,
    )
    is_capital_contribution = models.BooleanField(default=False)
    contribution = models.ForeignKey(
        CapitalContributions,
        on_delete = models.SET('DELETED'),
        related_name = 'contribution_moneyin',
        null = True,
    )
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class MoneyOutReceipts(models.Model):
    is_purchase = models.BooleanField(default=False)
    purchase = models.ForeignKey(
        PurchaseInvoices,
        on_delete = models.SET('DELETED'),
        related_name = 'purchase_moneyout',
        null = True,
    )
    is_fee = models.BooleanField(default=False)
    therapist = models.ForeignKey(
        Therapists,
        on_delete = models.SET('DELETED'),
        related_name = 'therapist_moneyout',
        null = True,
    )
    is_withdrawal = models.BooleanField(default=False)
    witdrawal = models.ForeignKey(
        CapitalWithdrawals,
        on_delete = models.SET('DELETED'),
        related_name = 'withdrawal_moneyout',
    )
    reference = models.TextField(max_length=500)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)