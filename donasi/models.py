from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Donasi(models.Model):
    penggalang = models.ForeignKey(User, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    target = models.BigIntegerField()
    foto = models.ImageField(upload_to='upload/')
    terkumpul = models.BigIntegerField(default=0)
    urlFoto = models.TextField(default='')
    is_approved = models.BooleanField(null=True, editable=False)

    def __str__(self):
        return self.nama

class Mendonasikan(models.Model):
    donatur = models.ForeignKey(User, on_delete=models.CASCADE)
    penerima = models.ForeignKey(Donasi, on_delete=models.CASCADE)
    nominal = models.BigIntegerField()

    def __str__(self):
        return self.donatur.username