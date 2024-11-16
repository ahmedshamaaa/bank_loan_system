from rest_framework import viewsets
from .models import LoanFund, Loan, LoanSettings
from .serializers import LoanFundSerializer, LoanSerializer, LoanSettingsSerializer

class LoanFundViewSet(viewsets.ModelViewSet):
    queryset = LoanFund.objects.all()
    serializer_class = LoanFundSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanSettingsViewSet(viewsets.ModelViewSet):
    queryset = LoanSettings.objects.all()
    serializer_class = LoanSettingsSerializer
