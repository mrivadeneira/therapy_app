from rest_framework import serializers
from .models import Assets, Clients, PaymentMethods, Bills, CreditNotes, MoneyInReceipts, MoneyOutReceipts, ProviderDetails, ProviderServices, Providers, PurchaseInvoices, Rentals, Partners, CapitalContributions, CapitalWithdrawals

class PartnersSerializer(serializers.ModelSerializer):
    partner_contributions = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    partner_withdrawals = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Partners
        fields = '__all__'

class CapitalContributionsSerializer(serializers.ModelSerializer):
    contribution_moneyin = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = CapitalContributions
        fields = '__all__'

class CapitalWithdrawalsSerializer(serializers.ModelSerializer):
    withdrawal_moneyout = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = CapitalWithdrawals
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    client_bill = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    client_rental = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Clients
        fields = '__all__'

class PaymentMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields = '__all__'

class RentalsSerializer(serializers.ModelSerializer):
    rental_bill = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Rentals
        fields = '__all__'

class BillsSerializer(serializers.ModelSerializer):
    bill_moneyin = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    bill_creditnote = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Bills
        fields = '__all__'

class CreditNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNotes
        fields = '__all__'

class ProvidersSerializer(serializers.ModelSerializer):
    provider_details = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    provider_services = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    provider_purchase = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Providers
        fields = '__all__'

class ProviderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderDetails
        fields = '__all__'

class ProviderServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderServices
        fields = '__all__'

class PurchaseInvoicesSerializer(serializers.ModelSerializer):
    purchase_asset = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = PurchaseInvoices
        fields = '__all__'

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class MoneyInReceiptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyInReceipts
        fields = '__all__'

class MoneyOutReceiptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyOutReceipts
        fields = '__all__'