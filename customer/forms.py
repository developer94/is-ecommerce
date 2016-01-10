from extra_views import InlineFormSet
from django import forms
from django.contrib.auth import models as auth_models
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from customer import models

class SignUpForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6,
                                widget=forms.PasswordInput,
                                label="Confirm password")

    class Meta:
        model = auth_models.User
        fields = ['email', 'username', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Register'))

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise ValidationError('You must confirm your password')

        if password1 != password2:
            raise ValidationError('Your confirmation password does not match')

        return password2

    def clean(self, *args, **kwargs):
        self.cleaned_data.pop('password2')

        return self.cleaned_data



class CustomerForm(forms.Form):
    username = forms.CharField(max_length=30, disabled=True)
    email = forms.EmailField(disabled=True)

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    gender = forms.ChoiceField(choices=models.Customer.GENDER_CHOICES)

    class Meta:
        model = models.Customer
        exclude = ('user',)



class CustomerInline(InlineFormSet):
    model = models.Customer
    fields = ['address', 'telephone', 'city', 'country', 'gender']

    can_delete = False
