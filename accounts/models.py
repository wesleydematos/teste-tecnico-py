from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import UnicodeUsernameValidator


class Account(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[username_validator],
    )
    nickname = models.CharField(max_length=20, default="")
    profile_picture = models.CharField(max_length=300, null=True)
    birthdate = models.DateField(null=True)
