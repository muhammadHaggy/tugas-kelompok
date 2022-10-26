from django.shortcuts import render
from donasi.models import Donasi
from django.http import HttpResponse
from django.core import serializers


def show_donasi(request):
    return render(request, "donasi.html")

def get_data_donasi(request):
    donasi = Donasi.objects.all()

    return HttpResponse(serializers.serialize('json', donasi))