from django.conf.urls import url

from company.views import (DashboardView, CompanySignUpView)
#ComponentCreateView,
                           #ComponentUpdateView, ComponentDeleteView, ComponentsListView)

app_name = "company"

urlpatterns = [
    url(r'^register/', CompanySignUpView.as_view(), name="register"),
    url(r'^dashboard/', DashboardView.as_view(), name="dashboard"),
    #url(r'^component/$', ComponentCreateView.as_view(), name="create_component"),
    #url(r'^component/(?P<pk>[\d]+)/$', ComponentUpdateView.as_view(), name="update_component"),
    #url(r'^component/(?P<pk>[\d]+)/$', ComponentDeleteView.as_view(), name="delete_component"),

    #url(r'^component/$', ComponentListView.as_view(), name="list_components"),
]
