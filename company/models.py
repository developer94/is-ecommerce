from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator

from account import models as account_models
from customer import models as customer_models

class Company(account_models.Account):
    name = models.CharField(max_length=50)

    PIB = models.CharField(max_length=9,
                           validators=[MinLengthValidator(9, message="PIB must be exactly 9 chars long.")],
                           unique=True)

    LK = models.CharField(max_length=50)
    uID = models.CharField(max_length=50, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'companies'


    def __unicode__(self):
        return '%s' % (self.name,)

