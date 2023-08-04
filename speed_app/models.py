from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.contrib.auth.models import User
import random
from .manager import CustomUserManager


def generate_account_number():
    return random.randint(1000000000, 9999999999)


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="", blank=True)
    firstname = models.CharField(max_length=255, default="", blank=True)
    lastname = models.CharField(max_length=255, default="", blank=True)
    phone = models.CharField(max_length=255)
    account_number = models.IntegerField(default=generate_account_number, unique=True)
    balance = models.IntegerField(default=1000)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Transaction(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.IntegerField()
    transact_user_account = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.transaction_type
