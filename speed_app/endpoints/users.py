from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from speed_app.models import CustomUser, Transaction, admin_required
from speed_app.serializers import UserSerializers, SendFundSerializer, DepositFundSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.http import Http404


# this only accessible by admin, it returns all users
class GetAllUsers(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(admin_required)
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)


# this is the endpoint for authenticated user to send funds to another user
class SendFunds(APIView):
    serializer_class = SendFundSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            transact_user_account = serializer.validated_data['transact_user_account']
            transaction_amount = serializer.validated_data['transaction_amount']
            try:
                recipient = CustomUser.objects.get(account_number=transact_user_account)
            except CustomUser.DoesNotExist:
                return Response({'message': 'Invalid account number'},
                                status=status.HTTP_400_BAD_REQUEST)

            if user.balance < transaction_amount:
                return Response({'message': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

            # Perform the transfer
            user.balance -= transaction_amount
            recipient.balance += transaction_amount

            # Save the changes
            user.save()
            recipient.save()

            return Response({'message': 'Funds transferred successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this is the endpoint for authenticated user to deposit funds
class DepositFunds(APIView):
    serializer_class = DepositFundSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            transaction_amount = serializer.validated_data['transaction_amount']
            if not transaction_amount:
                return Response({'message': 'Please enter an amount'}, status=status.HTTP_400_BAD_REQUEST)
            if transaction_amount < 0:
                return Response({'message': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)
            user.balance += transaction_amount
            user.save()
            return Response({'message': 'Funds deposited successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this is the endpoint for authenticated user to check balance
class CheckBalance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'message': f'Your balance is ${user.balance}'}, status=status.HTTP_200_OK)


# this is the endpoint for authenticated user to check his/her details
class UserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
