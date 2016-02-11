from django import forms
from django.core.urlresolvers import reverse

import autocomplete_light as al
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, HTML
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

from component.models import Available



class AvailableForm(al.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                'Component stock',
                FieldWithButtons('component', HTML('<a href="' + reverse('component:create') + '" class="btn btn-primary">New</a>')),
                Field('n_available', label="Number of components stocked")
            ),
        )

        super(AvailableForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Available
        fields = ('component', 'n_available',)



class ComponentForm(al.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                'Component',
                FieldWithButtons('component', HTML('<a href="' + reverse('component:create') + '" class="btn btn-primary">New</a>')),
                Field('n_available', title="Number of components stocked")
            ),
        )

        super(AvailableForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Available
        fields = ('component', 'n_available',)
