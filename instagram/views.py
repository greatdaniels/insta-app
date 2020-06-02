from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Images, Comments, Profiles
from django.contrib.auth.models import User
from .forms import PostComment, PostImagesForm, PostProfile


# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

# @login_required(login_url='/accounts/login/')
def index(request):
    images = Images.get_all_images()
    return render(request,'instagram/index.html',{'images':images})

# @login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profiles.filter_profile_by_id(user.id)
    title = f'{user.username}\'s Profile '
    images = Images.get_profile_images(user.id)
    return render(request, 'profile/profile.html',{'title':title,'users':user,'profile':profile,'images':images})

# @login_required(login_url='/accounts/login/')
def view_single_image(request,image_id):
    image = Images.get_image_by_id(image_id)
    comments = Comments.get_comment_by_image(image_id)
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


