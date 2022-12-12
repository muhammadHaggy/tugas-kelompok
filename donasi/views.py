from django.shortcuts import render
from donasi.models import Donasi, Mendonasikan
from donasi.forms import Pembayaran
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def show_donasi(request):    
    return render(request, 'donasi.html')

@login_required(login_url='/user/login')
def bayar_donasi(request, id):
    donasi = Donasi.objects.get(pk = id)
    context = {
        'penggalang': donasi.penggalang.first_name,
        'nama_donasi': donasi.nama,
        'deskripsi_donasi': donasi.deskripsi,
        'foto_donasi': donasi.foto,
        'terkumpul':donasi.terkumpul,
        'target': donasi.target,
        'form': Pembayaran(),
        'id': id,
    }
    return render(request, 'bayar_donasi.html', context)

# @login_required(login_url='/user/login')
# @csrf_exempt
def bayar_proses(request, id):
    if request.method == 'POST':
        form = Pembayaran(request.POST)
        donasi = Donasi.objects.get(pk = id)
        if form.is_valid():
            nominal = form.cleaned_data['nominal']
            donasi.terkumpul += nominal
            donasi.save()           

            Mendonasikan.objects.create(
                donatur=request.user,
                penerima=donasi,
                nominal=nominal
            )

    return JsonResponse({'message':"PAID"}, status=201)

def get_data_donasi(request):
    donasi = Donasi.objects.filter(is_approved=True)
    data = []

    for item in donasi:
        item.urlFoto = item.foto.url
        data.append({'pk': item.pk, 'fields': {'deskripsi': item.deskripsi, 'is_approved': item.is_approved, 'nama': item.nama, 'penggalang': item.penggalang.first_name, 'target': item.target, 'tipe': item.tipe, 'urlFoto': item.urlFoto, 'terkumpul': item.terkumpul,}}) 
    data = {'data': data}
    return JsonResponse(data)

def get_data_donasi_id(request, id):
    jumlah = Donasi.objects.get(pk = id).terkumpul
    return JsonResponse({'jumlah': jumlah})
