
from django.contrib import admin
from .models import User, LoanFund, Loan, LoanSettings

admin.site.register(User)
admin.site.register(LoanFund)
admin.site.register(Loan)
admin.site.register(LoanSettings)
