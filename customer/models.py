from __future__ import unicode_literals

from django.db import models
from account import models as account_models



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

    @property
    def details_provided(self):
        status = super(Customer, self).details_provided
        return status and all([self.first_name, self.last_name, self.gender])

