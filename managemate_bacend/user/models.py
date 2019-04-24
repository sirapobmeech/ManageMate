from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Super_user'),
        (2, 'HR'),
        (3, 'Normal_user')
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
