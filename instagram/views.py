from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Image, Comment, Profile
from django.contrib.auth.models import User
from .forms import PostComment, PostImagesForm, PostProfile



# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.get_all_images()
    return render(request,'instagram/index.html',{'images':images})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.filter_profile_by_id(user.id)
    title = f'{user.username}\'s Profile '
    images = Image.get_profile_images(user.id)
    return render(request, 'profile/profile.html',{'title':title,'users':user,'profile':profile,'images':images})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    title = 'Edit Profile'
    profile = User.objects.get(username=request.user)
    try:
        profile_details = Profile.get_profile_by_id(profile.id)
    except: 
        profile_details = Profile.filter_profile_by_id(profile.id)
    
    if request.method == 'POST':
        form = PostProfile(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = PostProfile()
    
    return render(request, 'profile/edit_profile.html', {'form':form, 'profile_details':profile_details})

@login_required(login_url='/accounts/login/')
def view_single_image(request,image_id):
    image = Image.get_image_by_id(image_id)
    comments = Comment.get_comment_by_image(image_id)
    current_user = request.user
    if request.method == 'POST':
        form = PostComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect('singleImage',image_id=image_id)
    else:
        form = PostComment()
    return render(request, 'photos.html',{'image':image,'form':form,'comments':comments})

@login_required(login_url='/accounts/login/')
def new_image(request): 
    current_user = request.user
    if request.method == 'POST':
        form = PostImagesForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
            return redirect('index',username=request.user)
    else:
        form = PostImagesForm()
    return render(request,'profile/post_image.html',{'form':form})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.get_profile_by_name( search_term)
        message = f'{search_term}'
        
        return render(request,'search.html',{'message':message,'profiles':profiles, 'search_term':search_term})
    else:
        message = 'Search Username'
        return render(request,'search.html',{'message':message})


