from django.conf.urls import url

from company.views import (DashboardView, CompanySignUpView, ItemCreateView,
                           ItemUpdateView, ItemDeleteView, ItemsListView)

app_name = "company"

urlpatterns = [
    url(r'^register/', CompanySignUpView.as_view(), name="register"),
    url(r'^dashboard/', DashboardView.as_view(), name="dashboard"),
    url(r'^item/$', ItemCreateView.as_view(), name="create_item"),
    url(r'^item/(?P<pk>[\d]+)/$', ItemUpdateView.as_view(), name="update_item"),
    url(r'^item/(?P<pk>[\d]+)/$', ItemDeleteView.as_view(), name="delete_item"),

    url(r'^items/$', ItemsListView.as_view(), name="list_items"),
]
