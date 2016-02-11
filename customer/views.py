from django.shortcuts import render

from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView

from customer.forms import SignUpForm, CustomerForm

from customer.models import Customer
from component.models import Category



class CustomerSignUpView(FormView):
    form_class = SignUpForm
    template_name = 'customer/signup.html'

    success_url = '/'

    def form_valid(self, form):
        user = User.objects.create_user(**form.cleaned_data)
        customer = Customer.objects.create(user=user)

        return super(CustomerSignUpView, self).form_valid(form)



class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/form.html'

    success_url = '/customer/browse'

    def get_object(self):
        return self.request.user.account

    def get_initial(self, *args, **kwargs):
        initial = super(UpdateView, self).get_initial(*args, **kwargs)
        initial['username'] = self.object.user.username
        initial['email'] = self.object.user.email

        return initial

    def form_valid(self, form):
        self.object.user.email = form.cleaned_data.pop('email')
        self.object.user.save()

        return super(CustomerUpdateView, self).form_valid(form)



class BrowseView(TemplateView):
    template_name = 'customer/browse.html'

    def get_context_data(self, **kwargs):
        context = super(BrowseView, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.all()

        return context

