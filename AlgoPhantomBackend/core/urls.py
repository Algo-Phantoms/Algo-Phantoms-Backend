from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
