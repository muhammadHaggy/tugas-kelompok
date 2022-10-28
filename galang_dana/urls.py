from django.urls import path
from galang_dana.views import *

app_name = 'galang_dana'

urlpatterns = [
    path('', show_galang_dana, name='show_galang_dana'),
]