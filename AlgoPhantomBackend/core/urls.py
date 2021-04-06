from django.urls import path
from .views import ChangePasswordView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # Change Password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
