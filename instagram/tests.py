from django.test import TestCase
from .models import Profile, Image, Comment
from django.contrib.auth.models import User
import datetime as dt

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'dan', email='dan@gmail.com', password='1234')
        self.user.save()
        
        self.profile = Profile(image= 'default.png', bio='the journey', user=self.user)
        self.profile.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
        
    def test_save_method(self):
        profile =Profile.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def tearDown(self):
        Profile.objects.all().delete()
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'dan', email='dan@gmail.com', password='1234')
        self.user.save()

        self.profile=Profile(image='default.png',bio='the journey',user=self.user)
        self.profile.save()
        
        self.image = Image(image='default.png',caption='testing1',pub_date='01/06/2020',profile=self.user,posted=auto_now())
        self.image.save_image()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_id(self):
        image_id = id
        self.image.objects.get(pk=id)
        self.assertTrue(pk=id)

    def tearDown(self):
        Image.objects.all().delete()
        
class CommentsTestClass(TestCase):

    def setup (self):
        self.user = User(username = 'dan', email='dan@gmail.com', password='1234')
        self.user.save()

        self.profile=Profile(image='default.png',bio='the journey',user=self.user)
        self.profile.save()

        self.comment=Comment(comment='interesting',image=self.image, user=self.profile,posted=auto_now())

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_save_method(self):
        self.comment.save_comment()
        comments =Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comments(self):
        self.comments.save_comments()
        self.comments.delete_comments()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 0)

    def tearDown(self):
        Comment.objects.all().delete()


        
        





