from django.urls import path
from .endpoints.auth import CustomRegisterView
from .endpoints.users import GetAllUsers

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('users/', GetAllUsers.as_view(), name='users'),
]
