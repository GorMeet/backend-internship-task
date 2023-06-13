from django.http.response import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import Calories
from .permissions import IsOwner
from .serializers import CalorieSerializer


class CaloriesViewSet(ModelViewSet):
    queryset = Calories.objects.all()
    serializer_class = CalorieSerializer
    permission_classes = [IsOwner | IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.role is not 'admin':
            serializer.save(user=request.user)
        else:
            serializer.save()
        return JsonResponse(serializer.data)

