from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(
        verbose_name="Номер телефона",
        max_length=128
    )
