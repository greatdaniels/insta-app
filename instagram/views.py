from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from . models import Images, Comments, Profiles


# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

# @login_required(login_url='/accounts/login/')
def index(request):
    images = Images.get_all_images()
    return render(request,'instagram/index.html',{'images':images})


