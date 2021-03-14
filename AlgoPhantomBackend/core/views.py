from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import User


def home(request):
    return HttpResponse('Hello')

