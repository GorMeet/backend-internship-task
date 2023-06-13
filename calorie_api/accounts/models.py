from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        user = ("user", "User")
        manager = ("manager", "Manager")
        admin = ("admin", "Admin")

    role = models.CharField(max_length=16, choices=Role.choices, default=Role.user)
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
