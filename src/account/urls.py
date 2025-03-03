from django.urls import path
from .views import *

urlpatterns = [
    path('send_otp', SendOTPView.as_view(), name='send_otp'),
    path('auth', Authentication.as_view(), name="auth"),
]
