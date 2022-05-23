from django.urls import path
from .views import *

app_name = 'accounts'


urlpatterns = [
    path('', LogInView, name='login'),
    path('logout', LogOutView, name='logout'),
    path('request-reset-email/', RequestResetEmail, name="request-reset-email"),
    path('reset-password/<uidb64>/<token>/', ResetPasswordView, name='reset-password'),
]