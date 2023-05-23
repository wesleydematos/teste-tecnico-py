from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    profile_picture = models.CharField(max_length=300, null=True)
    birthdate = models.DateField(null=True)
