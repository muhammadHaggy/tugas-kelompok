from datetime import datetime
from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        editable=False,
        unique=True,
    )
    tanggal_lahir = models.DateField(blank=True, default=datetime.now)
    bio_singkat = models.TextField(blank=True)