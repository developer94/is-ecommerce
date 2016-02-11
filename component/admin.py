from django.contrib import admin
from component.models import (Category, Component, Available,
                              Order, Reservation, ExpressedInterest)

import autocomplete_light

class ComponentAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(Component, fields='__all__')

admin.site.register(Category)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Available)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(ExpressedInterest)

