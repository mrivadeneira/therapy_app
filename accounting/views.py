from .models import CapitalContributions, CapitalWithdrawals, Partners, Clients, PaymentMethods, ProviderDetails, ProviderServices, Providers, PurchaseInvoices, Assets, Rentals, Bills, CreditNotes, MoneyInReceipts, MoneyOutReceipts
from .serializers import CapitalWithdrawalsSerializer, ClientsSerializer, PartnersSerializer, CapitalContributionsSerializer, PaymentMethodsSerializer, RentalsSerializer, BillsSerializer, CreditNotesSerializer, ProviderDetailsSerializer, ProviderServicesSerializer, ProvidersSerializer, PurchaseInvoicesSerializer, AssetsSerializer, MoneyInReceiptsSerializer, MoneyOutReceiptsSerializer
from rest_framework import generics

class PartnersAPIView(generics.ListCreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class PartnerChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer    

class CapitalContributionsAPIView(generics.ListCreateAPIView):
    queryset = CapitalContributions.objects.all()
    serializer_class = CapitalContributionsSerializer

class CapitalContributionsChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CapitalContributions.objects.all()
    serializer_class = CapitalContributionsSerializer

class CapitalWithdrawalsAPIView(generics.ListCreateAPIView):
    queryset = CapitalWithdrawals.objects.all()
    serializer_class = CapitalWithdrawalsSerializer

class CapitalWithdrawalsChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CapitalWithdrawals.objects.all()
    serializer_class = CapitalWithdrawalsSerializer

class ClientsAPIView(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class ClientChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class PaymentMethodsAPIView(generics.ListCreateAPIView):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer

class PaymentMethodChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer

class RentalsAPIView(generics.ListCreateAPIView):
    queryset = Rentals.objects.all()
    serializer_class = RentalsSerializer

class RentalChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rentals.objects.all()
    serializer_class = RentalsSerializer

class BillsAPIView(generics.ListCreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer

class BillChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer

class CreditNotesAPIView(generics.ListCreateAPIView):
    queryset = CreditNotes.objects.all()
    serializer_class = CreditNotesSerializer

class CreditNoteChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditNotes.objects.all()
    serializer_class = CreditNotesSerializer

class ProvidersAPIView(generics.ListCreateAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer

class ProviderChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProvidersSerializer

class ProviderDetailsAPIView(generics.ListCreateAPIView):
    queryset = ProviderDetails.objects.all()
    serializer_class = ProviderDetailsSerializer

class ProviderDetailsChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderDetails.objects.all()
    serializer_class = ProviderDetailsSerializer

class ProviderServicesAPIView(generics.ListCreateAPIView):
    queryset = ProviderServices.objects.all()
    serializer_class = ProviderServicesSerializer

class ProviderServicesChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProviderServices.objects.all()
    serializer_class = ProviderServicesSerializer

class PurchaseInvoicesAPIView(generics.ListCreateAPIView):
    queryset = PurchaseInvoices.objects.all()
    serializer_class = PurchaseInvoicesSerializer

class PurchaseInvoiceChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseInvoices.objects.all()
    serializer_class = PurchaseInvoicesSerializer

class AssetsAPIView(generics.ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

class AssetChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

class MoneyInReceiptsAPIView(generics.ListCreateAPIView):
    queryset = MoneyInReceipts.objects.all()
    serializer_class = MoneyInReceiptsSerializer

class MoneyInReceiptChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyInReceipts.objects.all()
    serializer_class = MoneyInReceiptsSerializer

class MoneyOutReceiptsAPIView(generics.ListCreateAPIView):
    queryset = MoneyOutReceipts.objects.all()
    serializer_class = MoneyOutReceiptsSerializer

class MoneyOutReceiptChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyOutReceipts.objects.all()
    serializer_class = MoneyOutReceiptsSerializer

