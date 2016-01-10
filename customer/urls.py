from django.conf.urls import url
from customer.views import CustomerSignUpView, BrowseView

app_name = "customer"

urlpatterns = [
    url(r'^register/', CustomerSignUpView.as_view(), name="register"),
    url(r'^browse/', BrowseView.as_view(), name="browse"),
]
