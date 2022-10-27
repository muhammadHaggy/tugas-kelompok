from django.shortcuts import render
from donasi.models import Donasi
from donasi.forms import Pembayaran
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
        'terkumpul':donasi.terkumpul,
        'target': donasi.target,
        'form': Pembayaran(),
        'id': id,
    }
    return render(request, 'bayar_donasi.html', context)

def bayar_proses(request, id):
    if request.method == 'POST':
        form = Pembayaran(request.POST)
        donasi = Donasi.objects.get(pk = id)
        if form.is_valid():
            nominal = form.cleaned_data['nominal']
            donasi.terkumpul += nominal
            donasi.save()

    return HttpResponse(serializers.serialize('json', donasi))

def get_data_donasi(request):
    donasi = Donasi.objects.all()
    for item in donasi:
            item.urlFoto = item.foto.url

    return HttpResponse(serializers.serialize('json', donasi))

def get_data_donasi_id(request, id):
    donasiTerkumpul = Donasi.objects.get(pk = id).terkumpul
    return HttpResponse(serializers.serialize('json', donasiTerkumpul))
