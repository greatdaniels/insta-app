from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')


