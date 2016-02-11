from django.conf.urls import url
from customer.views import CustomerSignUpView, BrowseView, CustomerUpdateView

app_name = "customer"

urlpatterns = [
    url(r'^register/', CustomerSignUpView.as_view(), name="register"),
    url(r'^browse/', BrowseView.as_view(), name="browse"),
    url(r'^update/', CustomerUpdateView.as_view(), name="update"),
]
