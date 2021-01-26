from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . import models
from .utils import *


class CoreRegisterSerializer(RegisterSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
        }

    def save(self,request):
        adapter=get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()
        adapter.save_user(request, user, self)
        send_mail(request, user.username, user, user.email)
        return user

    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)



   
class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model=Token
        fields = ('key','user',)

   