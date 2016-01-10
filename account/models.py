from __future__ import unicode_literals

from django.contrib.auth import models as auth_models
from django.db import models
from django_countries.fields import CountryField
from polymorphic.models import PolymorphicModel



class Account(PolymorphicModel):
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)

    address = models.CharField(max_length=140)
    telephone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = CountryField()

