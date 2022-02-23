from django.urls import path
from . import views

urlpatterns = [
    path('partners/', views.PartnersAPIView.as_view()),
    path('partners/<int:pk>', views.PartnerChangeAPIView.as_view()),
    path('capital_contributions/', views.CapitalContributionsAPIView.as_view()),
    path('capital_contributions/<int:pk>', views.CapitalContributionsChangeAPIView.as_view()),
    path('capital_withdrawals/', views.CapitalWithdrawalsAPIView.as_view()),
    path('capital_withdrawals/<int:pk>', views.CapitalWithdrawalsChangeAPIView.as_view()),
    path('clients/', views.ClientsAPIView.as_view()),
    path('clients/<int:pk>', views.ClientChangeAPIView.as_view()),
    path('paymentmethods/', views.PaymentMethodsAPIView.as_view()),
    path('paymentmethods/<int:pk>', views.PaymentMethodChangeAPIView.as_view()),
    path('rentals/', views.RentalsAPIView.as_view()),
    path('rentals/<int:pk>', views.RentalChangeAPIView.as_view()),
    path('bills/', views.BillsAPIView.as_view()),
    path('bills/<int:pk>', views.BillChangeAPIView.as_view()),
    path('creditnotes/', views.CreditNotesAPIView.as_view()),
    path('creditnotes/<int:pk>', views.CreditNoteChangeAPIView.as_view()),
    path('providers/', views.ProvidersAPIView.as_view()),
    path('providers/<int:pk>', views.ProviderChangeAPIView.as_view()),
    path('purchase_invoices/', views.PurchaseInvoicesAPIView.as_view()),
    path('purchases_invoices/<int:pk>', views.PurchaseInvoiceChangeAPIView.as_view()),
    path('assets/', views.AssetsAPIView.as_view()),
    path('assets/<int:pk>', views.AssetChangeAPIView.as_view()),
    path('moneyinreceipts/', views.MoneyInReceiptsAPIView.as_view()),
    path('moneyinreceipts/<int:pk>', views.MoneyInReceiptChangeAPIView.as_view()),
    path('moneyoutreceipts/', views.MoneyOutReceiptsAPIView.as_view()),
    path('moneyoutreceipts/<int:pk>', views.MoneyOutReceiptChangeAPIView.as_view()),
]

