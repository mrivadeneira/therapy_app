from django.urls import path
from . import views

urlpatterns = [
    path('patients/',views.PatientsAPIView.as_view()),
    path('patients/<int:pk>',views.PatientChangeAPIView.as_view()),
    path('patient_sessions/',views.SessionsAPIView.as_view()),
    path('patient_sessions/<int:pk>',views.PatientSessionsChangeAPIView.as_view()),
    path('patient_details/',views.PatientDetailsAPIView.as_view()),
    path('patient_details/<int:pk>',views.PatientDetailsChangeAPIView.as_view()),
    path('rooms/',views.RoomsAPIView.as_view()),
    path('rooms/<int:pk>',views.RoomChangeAPIView.as_view()),
    path('shifts/',views.ShiftsAPIView.as_view()),
    path('shifts/<int:pk>',views.ShiftChangeAPIView.as_view()),
]
