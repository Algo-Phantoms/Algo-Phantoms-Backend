from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse,HttpResponseRedirect
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
# Create your views here.

def home(request):

    return HttpResponse('Hello')


# def activate(request, uidb64, token):
#     # Verified Email-Id
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.save()
#         return HttpResponse('Email Verified')
#     else:
#         return HttpResponse("Activation Link is Invalid")