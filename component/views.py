from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from component.models import (ComponentAvailable, Order, Reservation,
                              ExpressedInterest)



class ComponentCreateView(CreateView):
    model = Component
    form_class = ComponentForm

    template_name = 'component/create.html'



class ComponentUpdateView(UpdateView):
    model = Component
    form = autocomplete_light.modelform_factory(Component, fields=('component',))



class ComponentDeleteView(DeleteView):
    model = Component



class ComponentsListView(ListView):
    model = Component

