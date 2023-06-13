from django.http import JsonResponse

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import (AuthTokenSerializer,
                                                  serializers)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.views import APIView, status
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import RegisterSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        if email and password:
            user, created = User.objects.get_or_create(username=email, email=email)
            if created:
                user.set_password(password)
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse(
                    {"token": token.key}, status=status.HTTP_201_CREATED
                )

        return JsonResponse(
            {"error": "Invalid username or password"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if email and password:
            user = User.objects.filter(email=email).first()

            if user is None or not user.check_password(password):
                return JsonResponse(
                    {"error": "Invalid email or password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"token": token.key}, status=status.HTTP_200_OK)

        return JsonResponse(
            {"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
