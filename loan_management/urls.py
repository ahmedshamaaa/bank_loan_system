from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanFundViewSet, LoanViewSet, LoanSettingsViewSet

router = DefaultRouter()
router.register(r'loan-funds', LoanFundViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'loan-settings', LoanSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
