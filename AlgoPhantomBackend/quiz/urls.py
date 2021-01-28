from django.urls import path
from .views import *

app_name='quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('question/<str:topic>/', QuizQuestion.as_view(), name='question'),
]