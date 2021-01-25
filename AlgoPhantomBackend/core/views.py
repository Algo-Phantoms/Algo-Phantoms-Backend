from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse,HttpResponseRedirect
# Create your views here.

def home(request):

    return HttpResponse('Hello')