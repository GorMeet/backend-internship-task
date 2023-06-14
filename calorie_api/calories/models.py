import json
from datetime import datetime

import requests
from accounts.models import User
from django.conf import settings
from django.db import models


class Calories(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    item = models.CharField(max_length=128)
    calories = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calories")
    is_extra = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.item

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.calories:
            url = settings.NUTRITIONX_API_BASE
            item = str(self.item)
            data = {"query": item}
            headers = {
                "Content-Type": "application/json",
                "X-APP-ID": settings.NUTRITIONX_API_APP_ID,
                "X-APP-KEY": settings.NUTRITIONX_API_KEY,
            }
            resp = requests.post(url=url, json=data, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                foods = data.get("foods", [])
                for food in foods:
                    self.calories = food.get("nf_calories", 0)
            else:
                self.calories = 0

        print(self.user)
        print(self.user.total_calories_today)
        print(self.user.calories_per_day)
        if self.user.total_calories_today > self.user.calories_per_day:
            self.is_extra = True
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ["-created_at"]
