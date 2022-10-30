from django.urls import path
from . import views

app_name = 'canwe'

urlpatterns = [
    path('', views.landingPage, name="landingPage"),
    path('canwe/', views.landingPage, name="landingPage"),
    path('send-question/', views.form_page, name='form_page'),
    path('question-page/', views.add_question, name='add_question'),
    path('json/', views.show_json, name='show_json'),
    path('show-question/', views.question_page, name='question_page'),
    path('delete/<int:i>/', views.delete, name='delete'),
]