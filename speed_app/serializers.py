from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser, Transaction


class CustomRegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=255, required=True)
    lastname = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(max_length=255)
    account_number = serializers.IntegerField(required=False, read_only=True)
    balance = serializers.IntegerField(required=False, read_only=True)
    phone = serializers.CharField(max_length=255, required=True)
    password1 = serializers.CharField(max_length=255, write_only=True)
    password2 = serializers.CharField(max_length=255, write_only=True)

    def validate_email(self, value):
        qs = CustomUser.objects.filter(email=value)
        if qs.exists():
            raise serializers.ValidationError("Email already exists")
        return value

    # def validate_username(self, value):
    #     # this is for case insensitive username
    #     qs = CustomUser.objects.filter(username__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("Username already exists")
    #     return value

    def validate_password1(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")
        return value

    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Invalid phone number,"
                                              " must be 10 digits long"
                                              " and contain only numbers")
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords must match")
        return data

    def get_cleaned_data(self, data):
        return {
            'first_name': data.get('first_name', ''),
            'last_name': data.get('last_name', ''),
            'username': data.get('username', ''),
            'email': data.get('email', ''),
            'phone': data.get('phone', ''),
            'account_type': 'user',  # 'user' or 'admin
            'password': data.get('password1', ''),
        }

    def save(self, request):
        if '@speedpay' in self.validated_data['email'].lower():
            user = CustomUser.objects.create(
                username=self.validated_data['username'].lower(),
                email=self.validated_data['email'].lower(),
                firstname=self.validated_data['firstname'].lower(),
                lastname=self.validated_data['lastname'].lower(),
                phone=self.validated_data['phone'],
                is_staff=True,
            )
            user.set_password(self.validated_data['password1'])
            user.save()
        else:
            user = CustomUser.objects.create(
                username=self.validated_data['username'].lower(),
                email=self.validated_data['email'].lower(),
                firstname=self.validated_data['firstname'].lower(),
                lastname=self.validated_data['lastname'].lower(),
                phone=self.validated_data['phone'],
            )
            user.set_password(self.validated_data['password1'])
            user.save()
        return user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'firstname', 'lastname', 'username', 'email', 'phone', 'account_number', 'balance']


class SendFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_amount', 'transact_user_account']


class DepositFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_amount']
