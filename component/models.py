from __future__ import unicode_literals

from django.db import models

from customer.models import Customer
from company.models import Company

class Category(models.Model):
    name = models.CharField(max_length=50)

    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'component categories'

    def __unicode__(self):
        return '%s' % (self.name,)



class Component(models.Model):
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)



class Available(models.Model):
    component = models.ForeignKey(Component)
    company = models.ForeignKey(Company)

    n_available = models.IntegerField()

    class Meta:
        verbose_name = 'component availability'
        verbose_name_plural = 'component availabilites'

        unique_together = ('component', 'company',)



class Reservation(models.Model):
    customer = models.ForeignKey(Customer)
    company = models.ForeignKey(Company)

    component = models.ForeignKey(Component)
    n_reserved = models.IntegerField()

    date = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=140)



class Order(models.Model):
    component = models.ForeignKey(Component)
    customer = models.ForeignKey(Customer)
    company = models.ForeignKey(Company)
    n_bought = models.IntegerField()

    date = models.DateField(auto_now_add=True)

    status = models.CharField(max_length=140)


class ExpressedInterest(models.Model):
    component = models.ForeignKey(Component)
    customer = models.ForeignKey(Customer)
    company = models.ForeignKey(Company)

    date = models.DateField(auto_now_add=True)

