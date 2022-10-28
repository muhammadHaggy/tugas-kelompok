from django.shortcuts import render

# Create your views here.
def show_galang_dana(request):
    return render(request, 'galang-dana.html')