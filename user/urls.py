from django.urls import path
from .views import approve, index, login_user, moderator, pending_task_json, register, reject

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('pending_task/', pending_task_json, name='pending_task_json'),
    path('moderator/', moderator, name='moderator'),
    path('moderator/approve/<int:pk>', approve, name='approve'),
    path('moderator/reject/<int:pk>', reject, name='reject'),

]