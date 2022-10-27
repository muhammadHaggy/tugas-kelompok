from django.shortcuts import render
from donasi.models import Donasi
from django.http import HttpResponse
from django.core import serializers


def show_donasi(request):    
    return render(request, 'donasi.html')

def bayar_donasi(request, id):
    donasi = Donasi.objects.get(pk = id)
    context = {
        'nama_donasi': donasi.nama,
        'deskripsi_donasi': donasi.deskripsi,
        'foto_donasi': donasi.foto,
    }
    return render(request, 'bayar_donasi.html', context)
    # return render(request, 'bayar_donasi.html')

def get_data_donasi(request):
    donasi = Donasi.objects.all()
    for item in donasi:
            item.urlFoto = item.foto.url

    return HttpResponse(serializers.serialize('json', donasi))