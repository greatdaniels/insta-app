from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField

class Profile(models.Model):
    image = ImageField(blank = True)
    bio = HTMLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod 
    def get_profile_by_name(cls, search_term):
        profile = cls.objects.filter(user__username__icontains = search_term)
        return profile
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    
    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    
    
class Image(models.Model):
    image = ImageField(blank = True,)
    caption = HTMLField()
    posted = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-posted',)
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod  
    def get_image_by_id(cls,id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls,profile):
        images = Image.objects.filter(profile__pk= profile)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
    
    
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_comment(self):
        self.save()
    
    def delete_comments(self):
        self.delete()
        
    @classmethod
    def get_comment_by_image(cls,id):
        comment = Comment.objects.filter(image__pk = id)
        return comment


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
    
    
