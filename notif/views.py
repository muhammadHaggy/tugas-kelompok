import datetime

from django.shortcuts import render
from notif.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@login_required(login_url='/user/')
def show_notif(request):
    data = Item.objects.all()
    context = {
        'list_todo': data,
        'username': request.user.username,
    }
    return render(request, "notif.html", context)


@staff_member_required
def create_notif(request):
    if request.method == 'POST':
        title = request.POST.get('notif')
        description = request.POST.get('description')
        user = request.user
        obj = Item.objects.create (title=title, description=description, user=user)
        obj.save()
        response = HttpResponseRedirect(reverse("notif:show_notif"))
    return render(request, 'tambah2.html')

def delete_notif(request, pk):
    Item.objects.filter(id=pk).delete()
    return redirect('notif:show_notif')

@login_required(login_url='/user/')
def show_json(request):
    item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', item), content_type='application/json')

def add_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        item = Item(title=title, description=description, user=user)
        item.save()
    return JsonResponse({"instance": "Proyek Dibuat"},status=200)

@csrf_exempt    
def delete(request, pk):
    if request.method == 'DELETE':
        Item.objects.filter(id=pk).delete()
    return JsonResponse({"instance": "Proyek Dihapus"},status=200)