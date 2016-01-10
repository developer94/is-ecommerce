from django.shortcuts import render

from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from customer.forms import SignUpForm

from customer.models import Customer
from company.models import ComponentCategory



class CustomerSignUpView(FormView):
    form_class = SignUpForm
    template_name = 'customer/signup.html'

    success_url = '/'

    def form_valid(self, form):
        user = User.objects.create_user(**form.cleaned_data)
        customer = Customer.objects.create(user=user)

        return super(CustomerSignUpView, self).form_valid(form)



class BrowseView(TemplateView):
    template_name = 'customer/browse.html'

    def get_context_data(self, **kwargs):
        context = super(BrowseView, self).get_context_data(**kwargs)

        context['categories'] = ComponentCategory.objects.all()

        return context

