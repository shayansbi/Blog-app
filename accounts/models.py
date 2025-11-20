from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='static/img',
                                null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)