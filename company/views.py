from django.db import transaction
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import (FormView, CreateView, UpdateView,
                                       DeleteView)
import autocomplete_light

from account.forms import UserForm
from company.forms import CompanyForm
from component.models import Available
from component.forms import AvailableForm



class DashboardView(TemplateView):
    template_name = 'company/dashboard.html'



class CompanySignUpView(FormView):
    template_name = 'company/signup.html'
    success_url = '/'

    # override the default form insertion,
    # we're doing manual work with sending custom forms
    # NOTE: All this should be replaced with inline formset at one point
    def get_form(self):
        return None

    def get_context_data(self, *args, **kwargs):
        """
        Load the appropriate forms into context.
        If they're already in, it means we're getting back bound forms with
        validation errors.
        """
        context = super(CompanySignUpView, self).get_context_data(*args, **kwargs)

        if('user_form' not in context):
            context['user_form'] = UserForm(prefix="user")

        if('company_form' not in context):
            context['company_form'] = CompanyForm(prefix="company")

        return context


    def post(self, *args, **kwargs):
        user_form = UserForm(self.request.POST, prefix="user")
        company_form = CompanyForm(self.request.POST, prefix="company")

        if user_form.is_valid() and company_form.is_valid():
            return self.form_valid(user_form, company_form)
        else:
            return self.render_to_response(self.get_context_data(user_form=user_form, company_form=company_form))



    def form_valid(self, form, company_form):
        with transaction.atomic():
            company = company_form.save(commit=False)
            user = form.save()
            company.user = user
            company.save()

        return super(CompanySignUpView, self).form_valid(form)



class ItemCreateView(CreateView):
    model = Available
    form_class = AvailableForm

    template_name = 'company/create.html'



class ItemUpdateView(UpdateView):
    model = Available
    form = autocomplete_light.modelform_factory(Available, fields=('component',))



class ItemDeleteView(DeleteView):
    model = Available



class ItemsListView(ListView):
    model = Available

