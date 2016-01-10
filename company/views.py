from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from account.forms import UserForm
from company.forms import CompanyForm



class DashboardView(TemplateView):
    template_name = 'company/dashboard.html'



class CompanySignUpView(FormView):
    template_name = 'company/signup.html'
    form_class = UserForm

    def get_context_data(self, *args, **kwargs):
        context = super(CompanySignUpView, self).get_context_data(*args, **kwargs)

        context['form'] = UserForm(prefix="user")
        context['company_form'] = CompanyForm(prefix="company")

        return context


    def post(self, *args, **kwargs):
        form = UserForm(self.request.POST, prefix="user")
        company_form = CompanyForm(self.request.POST, prefix="company")

        if form.is_valid() and company_form.is_valid():
            return self.form_valid(form, company_form)
        else:
            return self.render_to_response(self.get_context_data(form=form, company_form=company_form))



    def form_valid(self, form, company_form):
        import pdb
        pdb.set_trace()

        company = company_form.save(commit=False)
        user = form.save()
        company.user = user
        company.save()

        return super(CompanySignUpView, self).form_valid(form)

