from django.urls import path
from notif.views import show_notif, delete_notif
from notif.views import create_notif, show_json, add_ajax, delete

app_name = 'notif'

urlpatterns = [
    path('', show_notif, name='show_notif'),
    path('create-notification/', create_notif, name='create-notification'),
    path('delete-notification/<int:pk>', delete_notif, name='delete-notif'),
    path('json/', show_json, name='show_json'),
    path('add_ajax/', add_ajax, name='add_ajax'),  
    path('delete/<int:pk>/', delete, name='delete'),
]