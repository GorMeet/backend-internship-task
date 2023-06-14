from accounts.models import User
from accounts.permissions import IsOwner
from django.http.response import JsonResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Calories
from .serializers import CalorieSerializer


class CaloriesViewSet(ModelViewSet):
    queryset = Calories.objects.all()
    serializer_class = CalorieSerializer
    permission_classes = [IsOwner | IsAdminUser]

    def get_queryset(self):
        for item in self.queryset:
            print(item.user.id, item.user.total_calories_today)
        if self.request.user.role == User.Role.admin:
            return self.queryset

        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.role != User.Role.admin:
            serializer.save(user=request.user)
        else:
            serializer.validated_data["user_id"] = request.data["user"]
            serializer.save()
        return JsonResponse(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if request.user.role == User.Role.admin:
            serializer.validated_data["user_id"] = request.data["user"]
        serializer.save()
        return JsonResponse(serializer.data)
