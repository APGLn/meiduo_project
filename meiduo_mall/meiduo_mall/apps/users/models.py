from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """自定义用户模型类"""
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'tb_user'

    def __str__(self):
        return self.username
