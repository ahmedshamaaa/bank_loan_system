
from django.test import TestCase
from django.contrib.auth.models import User
from .models import LoanFund, Loan, LoanParameters

class LoanManagementTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.fund = LoanFund.objects.create(provider=self.user, amount=10000)
        self.params = LoanParameters.objects.create(
            created_by=self.user, max_amount=5000, min_amount=100, interest_rate=5, max_term_months=60, min_term_months=6)

    def test_loan_creation(self):
        loan = Loan.objects.create(customer=self.user, fund=self.fund, amount=500, term_months=12, interest_rate=5)
        self.assertEqual(loan.customer.username, 'testuser')
        self.assertAlmostEqual(loan.calculate_monthly_payment(), 42.87, 2)
