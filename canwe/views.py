from django.shortcuts import render, redirect
from django.urls import reverse

def landingPage(request):
    return render(request, 'landingPage.html')
