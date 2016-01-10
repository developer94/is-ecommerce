from django.views.generic.base import RedirectView, TemplateView
from django.core.urlresolvers import reverse
from customer.models import Customer

class LandingPageView(TemplateView):
    template_name = "landing.html"

class HomeView(RedirectView):
    def get_redirect_url(self):
        if self.request.user.is_anonymous():
            return reverse('landing')

        if isinstance(self.request.user.account, Customer):
            return reverse('customer:browse')

        if isinstance(self.request.user.account, Company):
            return reverse('company:dashboard')

