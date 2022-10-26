from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from donasi.models import Donasi
from django.core import serializers
def index(request):
    return redirect(reverse('user:login_user'))
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("canwe:landingPage"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('user:login_user')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='user/login')
def pending_task_json(request):
    if request.user.is_staff:
        data_donasi_pending = Donasi.objects.filter(is_approved__isnull=True).all()
        for item in data_donasi_pending:
            item.urlFoto = item.foto.url
        return HttpResponse(serializers.serialize("json", data_donasi_pending), content_type="application/json")
    return JsonResponse({'error': 'User bukan staff canwe'})

@login_required(login_url='user/login')
def moderator(request):
    return render(request, 'moderation.html')

@login_required(login_url='user/login')
def reject(request, pk):
    if request.method == "GET" and request.user.is_staff:
        donasi = Donasi.objects.filter(pk=pk).update(is_approved=False)
    
    return HttpResponse()

@login_required(login_url='user/login')
def approve(request, pk):
    if request.method == "GET" and request.user.is_staff:
        donasi = Donasi.objects.filter(pk=pk).update(is_approved=True)
    
    return HttpResponse()

