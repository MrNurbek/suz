from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# from smart_selects.db_fields import ChainedForeignKey


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['last_name']

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username


class Logat(models.Model):
    name = models.TextField(max_length=2255, blank=True, null=True)
    text = models.TextField(max_length=2255, blank=True, null=True)

    def __str__(self):
        return self.name