from __future__ import unicode_literals

from django.db import models
from account import models as account_models
from company import models as company_models



class Customer(account_models.Account):
    first_name = models.CharField(null=True, max_length=10)
    last_name = models.CharField(null=True, max_length=10)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)



class ComponentReservation(models.Model):
    customer = models.ForeignKey(Customer)
    component = models.ForeignKey(company_models.Component)
    company = models.ForeignKey(company_models.Company)

    date = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=140)

