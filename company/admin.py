from django.contrib import admin
from company.models import Company, ComponentCategory, Component, ComponentAvailable


admin.site.register(Company)
admin.site.register(ComponentCategory)
admin.site.register(Component)
admin.site.register(ComponentAvailable)

