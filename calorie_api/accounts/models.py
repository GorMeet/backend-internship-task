from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        user = ("user", "User")
        manager = ("manager", "Manager")
        admin = ("admin", "Admin")

    role = models.CharField(max_length=16, choices=Role.choices, default=Role.user)
    email = models.EmailField(unique=True, blank=False, null=False)
    calories_per_day = models.PositiveIntegerField(default=0, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def total_calories_today(self):
        return self.calories.filter(created_at__date=date.today()).aggregate(
            total=models.Sum("calories")
        )["total"]
