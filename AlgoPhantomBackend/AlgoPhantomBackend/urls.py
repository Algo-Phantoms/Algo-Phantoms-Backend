"""AlgoPhantomBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_auth.registration.views import VerifyEmailView, RegisterView, LoginView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('quiz/',include('quiz.urls')),
    
    path('rest-auth/', include('rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/login/', LoginView.as_view(), name='account_login'),
    path('registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/', RegisterView.as_view(), name='account_signup'),
    path('rest-auth/account-confirm-email/', VerifyEmailView.as_view(),name='account_email_verification_sent'),
    url('rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),name='account_confirm_email'),

]
