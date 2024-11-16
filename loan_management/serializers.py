from rest_framework import serializers
from .models import LoanFund, Loan, LoanSettings

class LoanFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFund
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class LoanSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanSettings
        fields = '__all__'
