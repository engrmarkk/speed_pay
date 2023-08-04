from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import User
import random


def generate_account_number():
    return random.randint(1000000000, 9999999999)


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, unique=True)
    account_number = models.IntegerField(
        default=generate_account_number, unique=True
    )
    account_balance = models.IntegerField(default=20000)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.IntegerField()
    transact_user = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username


"""
from extensions import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    account_number = db.Column(db.Integer, unique=True, nullable=False)
    account_balance = db.Column(db.Integer, default=20000)
    is_admin = db.Column(db.Boolean, default=False)
    transacts = db.relationship("Transaction",cascade="all, delete", back_populates="users", lazy=True)
    
    
from extensions import db
import datetime


class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow()
    )
    transaction_amount = db.Column(db.Integer, nullable=False)
    transact_user = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    users = db.relationship("User", back_populates="transacts")

"""