import json
from django.shortcuts import render
from donasi.models import Donasi
from user.models import UserDetails
from galang_dana.forms import FormGalangDana

from django.http import HttpResponse, HttpResponseNotFound
from django.http.response import JsonResponse
from django.core import serializers

from django.contrib.auth.decorators import login_required


# Create your views here.
def show_galang_dana(request):
    return render(request, 'galang-dana.html')

@login_required(login_url='/user/login')
def show_buat_galang_dana(request):
    context = {'form': FormGalangDana}
    return render(request, 'buat-galang-dana.html', context)

def create_galang_dana(request):
    if request.method == "POST":

        form = FormGalangDana(request.POST, request.FILES)

        if form.is_valid():
            new_donasi = Donasi(
                penggalang=request.user,
                tipe=form.cleaned_data['tipe'],
                nama=form.cleaned_data['judul'],
                deskripsi=form.cleaned_data['deskripsi'],
                target=form.cleaned_data['target'],
                foto=form.cleaned_data['foto']
            )
            new_donasi.save()
            return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def create_galang_dana_flutter(request):
    if request.method == 'POST':
        new_item = json.loads(request.body)
        
        new_donasi = Donasi(
            penggalang=request.user,
            tipe=new_item['tipe'],
            nama=new_item['judul'],
            deskripsi=new_item['deskripsi'],
            target=new_item['target'],
            foto=new_item['foto']
        )
        new_donasi.save()

        return JsonResponse({'instance': 'Galang Dana Berhasi Dibuat!'}, status=200)

def get_user_count_json(request):
    all_donatur = UserDetails.objects.all()
    return HttpResponse(serializers.serialize("json", all_donatur), content_type="application/json")