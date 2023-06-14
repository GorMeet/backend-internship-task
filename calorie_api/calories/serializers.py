from rest_framework.authtoken.serializers import serializers

from .models import Calories


class CalorieSerializer(serializers.ModelSerializer):
    calories = serializers.IntegerField(required=False)

    class Meta:
        model = Calories
        fields = ["id", "created_at", "item", "calories", "user", "is_extra"]
        read_only_fields = [
            "user",
        ]
