from django.http import HttpResponseRedirect, HttpResponseNotFound
from canwe.forms import ContactForm
from .models import Contact
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

# show landing page
def landingPage(request):
    return render(request, 'landingPage.html')

# show send question page
def form_page(request):
    context = {}
    context['form']= ContactForm()
    return render(request, "form_page.html", context)

@staff_member_required
def question_page(request):
    context = {}
    context['form']= ContactForm()
    return render(request, "question_page.html", context)

@login_required(login_url='/user/login')
def add_question(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        question = request.POST.get('question')

        obj = Contact(user=request.user, name=name, email=email, question=question)
        obj.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/user/login')
def show_json(request):
    item = Contact.objects.all()
    return HttpResponse(serializers.serialize('json', item), content_type="application/json")

@staff_member_required
def delete(request, i):
    y = Contact.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/show-question/')