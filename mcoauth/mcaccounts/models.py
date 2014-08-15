from django.db import models
from django.contrib.auth import get_user_model


class MinecraftAccount(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='minecraft_accounts')
    name = models.CharField(max_length=255)
    profile = models.CharField(max_length=75)
    profile_id = models.CharField(max_length=32, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
