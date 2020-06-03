from django import forms
from .models import Profile, Comment, Image

class PostImagesForm(forms.ModelForm):
    image = forms.ImageField()
    caption = forms.CharField(max_length=100)
    class Meta: 
        model = Image
        exclude = ['posted','profile']
        
        
class PostComment(forms.ModelForm):
    class Meta: 
        model = Comment
        exclude = ['image','posted','user']

class PostProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        

        