from django.contrib import admin
from donasi.models import Donasi, Mendonasikan
from .models import UserDetails

admin.site.register(Donasi)
admin.site.register(Mendonasikan)
admin.site.register(UserDetails)