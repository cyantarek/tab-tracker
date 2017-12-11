from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .api.serializers import RegistrationSerializer, LoginSerializer


def status_view():
	status = {
		"message": "status OK!"
	}
	return JsonResponse(status)


class RegisterAPIView(CreateAPIView):
	serializer_class = RegistrationSerializer
	queryset = User.objects.all()

class LoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = LoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return JsonResponse(new_data)