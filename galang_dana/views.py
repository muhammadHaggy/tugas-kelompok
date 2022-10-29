from django.shortcuts import render
from user.models import UserDetails

from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers


# Create your views here.
def show_galang_dana(request):
    return render(request, 'galang-dana.html')

def show_buat_galang_dana(request):
    return render(request, 'buat-galang-dana.html')

def get_user_count_json(request):
    all_donatur = UserDetails.objects.all()
    return HttpResponse(serializers.serialize("json", all_donatur))