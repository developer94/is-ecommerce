from django.contrib.auth.models import Group

Group.objects.get_or_create(name='customer')
Group.objects.get_or_create(name='company')
Group.objects.get_or_create(name='staff')