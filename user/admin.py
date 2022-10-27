from django.contrib import admin
from donasi.models import Donasi
from .models import UserDetails

admin.site.register(Donasi)
admin.site.register(UserDetails)