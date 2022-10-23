from django.urls import path
from .views import login_user, register

app_name = 'user'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
]