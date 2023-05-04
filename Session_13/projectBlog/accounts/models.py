from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Profile(AbstractUser):
    age = models.PositiveIntegerField(help_text="User Age", blank=True, null=True)
