from .models import Patients, PatientDetails, PatientSessions, Rooms, Shifts
from .serializers import PatientsSerializer, PatientDetailsSerializer, PatientSessionsSerializer, RoomsSerializer, ShiftsSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
#from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

class PatientsAPIView(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lastname']
    #authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions, TokenHasReadWriteScope]


class PatientChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class SessionsAPIView(generics.ListCreateAPIView):
    queryset = PatientSessions.objects.all()
    serializer_class = PatientSessionsSerializer

class PatientSessionsChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientSessions.objects.all()
    serializer_class = PatientSessionsSerializer

class PatientDetailsAPIView(generics.ListCreateAPIView):
    class DetailsFilter(FilterSet):
        class Meta:
            model = PatientDetails
            fields = '__all__'
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer
    filter_class = DetailsFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['=id_document_n', '$email',]
    ordering_fields = ('patient',)

class PatientDetailsChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

class RoomsAPIView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class RoomChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class ShiftsAPIView(generics.ListCreateAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer

class ShiftChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer