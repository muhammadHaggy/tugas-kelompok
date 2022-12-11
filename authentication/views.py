from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

from user.models import UserDetails


def login_logic(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                # Insert any extra data if you want to pass data to Flutter
                "is_admin": user.is_staff
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
        }, status=401)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return login_logic(request, username, password)
    else:
        return JsonResponse({
            "status": False,
            "message": "Use POST request!"
        })


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = user.username
            user.save()
            UserDetails(user=user).save()
            return login_logic(request, user.username, request.POST['password1'])
        else:
            return JsonResponse({"status": False, "message": form.errors.as_text()})

    return JsonResponse({"status": False, "message": "Use POST request!"})
