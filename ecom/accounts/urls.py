from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserAccountsAV

urlpatterns = [
    path('token/',obtain_auth_token,name="auth_token"),
    path('handle/',UserAccountsAV.as_view(),name="customer_account")
]