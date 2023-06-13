from datetime import datetime
from django.db import models

from accounts.models import User


class Calories(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    item = models.CharField(max_length=128)
    calories = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calories')
    is_extra = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ["-created_at"]
