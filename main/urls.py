from django.urls import path, include
from django.views import View
from main.views import *

urlpatterns = [
    path('login/', login.as_view(), name='login'),
    path('test/', test.as_view(), name='test'),
    path('otpcheck/', otp.as_view, name='check_otp'),
    path('sendotp/', otp.as_view, name='send_otp'),
    path('upgrade/', upgrade.as_view, name='user_upgrade'),
    path('changepass/', changePass.as_view, name='change_password'),
    path('updateData/', changePass.as_view, name='updateData'),
]
