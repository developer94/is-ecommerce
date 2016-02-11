from __future__ import unicode_literals

from django.apps import AppConfig

import autocomplete_light.shortcuts as al

class ComponentConfig(AppConfig):
    name = 'component'

    def ready(self):
        from component.models import Category, Component

        al.register(Category, search_fields=['name'])
        al.register(Component, search_fields=['name'])

