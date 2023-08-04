from dj_rest_auth.registration.views import RegisterView
from speed_app.serializers import CustomRegisterSerializer
from rest_framework.permissions import AllowAny


class CustomRegisterView(RegisterView):
    permission_classes = [AllowAny]
    serializer_class = CustomRegisterSerializer
