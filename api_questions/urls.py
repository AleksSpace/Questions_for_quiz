from django.urls import path

from api_questions.views import my_view

urlpatterns = [
    path('questions_num', my_view, name='questions'),
]
