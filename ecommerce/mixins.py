from django.views.generic.edit import ProcessFormView

class ProcessMultipleFormsView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        forms = self.get_forms()

        for form in forms:
            if form.is_valid() == False:
                # return only the form that broke first in case of an error
                # ideally we should report all of them, and handle the invalid
                # error display for all of the forms, but we're short on time
                # here. What will happen: the errors will appear on the first
                # form that had them. On the next submit, they'll appear on the
                # following one, and so on.
                # FUCK
                # FUCK FUCK FUCK FUCK FUCK FUCK
                # imam samo dva modela koja uklapam, mogu komotno inlineformset...
                # damn cek da vidim
                # ZNAO SAM DA JE ANTIPATTERN
                # dobro, svaki dan naucis nesto novo
                # u sustini ovo je i bio cilj, ha, sad se osecam bolje :D
                return self.form_invalid(form)

            return self.form_valid(forms)

