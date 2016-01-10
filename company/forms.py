from django import forms
from django_countries.fields import CountryField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from company import models



class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        self.fields['LK'].label = 'Owner\'s personal ID number:'

    class Meta:
        model = models.Company
        exclude = ('user', 'uID')

