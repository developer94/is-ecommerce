from django.conf.urls import url

from company.views import DashboardView, CompanySignUpView

app_name = "company"

urlpatterns = [
    url(r'^register/', CompanySignUpView.as_view(), name="register"),
    url(r'^dashboard/', DashboardView.as_view(), name="browse"),
]
