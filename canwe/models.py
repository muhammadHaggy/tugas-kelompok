from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default="")
    email = models.EmailField(max_length=200, default="")
    question = models.TextField(max_length=2000, default="")