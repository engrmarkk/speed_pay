from dj_rest_auth.registration.views import RegisterView
from speed_app.serializers import CustomRegisterSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
