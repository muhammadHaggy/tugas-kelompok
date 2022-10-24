from django.shortcuts import render
 
# Create your views here.
def show_notifikasi(request):
    return render(request, 'notifikasi.html')