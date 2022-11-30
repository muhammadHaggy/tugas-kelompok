from django.urls import path
from .views import profile_dashboard_json ,approve, index, login_user, moderator, pending_task_json, register, reject, logout_user, profile_dashboard

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('pending_task/', pending_task_json, name='pending_task_json'),
    path('moderator/', moderator, name='moderator'),
    path('moderator/approve/<int:pk>', approve, name='approve'),
    path('moderator/reject/<int:pk>', reject, name='reject'),
    path('profile/json', profile_dashboard_json, name='profile-json'),
    path('profile/', profile_dashboard, name='profile'),

]