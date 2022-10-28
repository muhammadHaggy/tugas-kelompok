from urllib import response
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
from django.contrib.auth.models import User
from user.forms import UserDetailsForm, UserForm
from user.models import UserDetails
from notif.models import Item


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
            # response.set_cookie('last_login', str(datetime.datetime.now()))
            request.session['last_login'] = str(datetime.datetime.now())
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            UserDetails(user=user).save()
            return redirect('user:login_user')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='user/login')
def pending_task_json(request):
    if request.user.is_staff:
        data_donasi_pending = Donasi.objects.filter(is_approved__isnull=True).all()
        data = []
        for item in data_donasi_pending:
            item.urlFoto = item.foto.url
            data.append({'pk': item.pk, 'fields': {'deskripsi': item.deskripsi, 'is_approved': item.is_approved, 'nama': item.nama, 'penggalang': item.penggalang.username, 'target': item.target, 'tipe': item.tipe, 'urlFoto': item.urlFoto}}) 
            json = serializers.serialize("json", data_donasi_pending)
        # return HttpResponse(json, content_type="application/json")
        data = {'data': data}
        return JsonResponse(data)
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

@login_required(login_url='user/login')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('user:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='user/login')
def profile_dashboard(request):
    user = User.objects.get(pk = request.user.pk)
    user_detail = UserDetails.objects.get(user=user)
    if request.method == "POST":
        user_detail_form = UserDetailsForm(request.POST, instance=user_detail)
        user_form = UserForm(request.POST, instance=user)
        if (user_form.is_valid() and user_detail_form.is_valid()):
            user_form.save()
            user_detail_form.save()
        # user.username = request.POST['username']
        # user.first_name = request.POST['firstname']
        # user.last_name = request.POST['lastname']
        # user.email = request.POST['email']
        # user_detail.tanggal = request.POST['tanggal']
        # user_detail.bio = request.POST['bio']
        # user.save()
        # user_detail.save()
        return HttpResponse()
    user_detail_form = UserDetailsForm(instance=user_detail)
    user_form = UserForm(instance=user)
    context = {'user_detail': user_detail, 'user_form': user_form, 'user_detail_form': user_detail_form, 'last_login':request.session['last_login']}
    return render(request, 'profile.html', context)