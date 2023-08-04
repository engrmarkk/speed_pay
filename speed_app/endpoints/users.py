from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from speed_app.models import CustomUser
from speed_app.serializers import UserSerializers


class GetAllUsers(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)
