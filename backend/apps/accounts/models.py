from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from apps.core.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.email