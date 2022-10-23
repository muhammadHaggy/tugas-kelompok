from django.db import models
from django.contrib.auth.models import User

class Donasi(models.Model):
    penggalang = models.ForeignKey(User, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    target = models.BigIntegerField()
    foto = models.ImageField()

    def __str__(self):
        return self.name
