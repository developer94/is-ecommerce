from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from account import models



class AccountForm(ModelForm):
    class Meta:
        model = models.Account
        exclude = ('user', )



class UserForm(ModelForm):
    password = forms.CharField(min_length=6,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=6,
                                widget=forms.PasswordInput,
                                label="Confirm password")

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']


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
