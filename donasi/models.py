from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from moderation.db import ModeratedModel

class Donasi(ModeratedModel):
    penggalang = models.ForeignKey(User, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    target = models.BigIntegerField()
    foto = models.ImageField(upload_to='upload/')
    terkumpul = models.BigIntegerField(default=0)
    urlFoto = models.TextField(default='')

    def __str__(self):
        return self.nama
