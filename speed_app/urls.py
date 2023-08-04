from django.urls import path
from .endpoints.auth import CustomRegisterView
from .endpoints.users import GetAllUsers, SendFunds, DepositFunds
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('users/', GetAllUsers.as_view(), name='users'),
    path('send-funds/', SendFunds.as_view(), name='send-funds'),
    path('deposit-funds/', DepositFunds.as_view(), name='deposit-funds'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
