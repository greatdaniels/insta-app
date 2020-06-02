from django.test import TestCase
from .models import Profiles, Images, Comments
from django.contrib.auth.models import User
import datetime as dt

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'pip', email='g@gmail.com', password='pip2')
        self.user.save()
        
        self.profile = Profiles(image= '/posts', bio='TGOD', user=self.user)
        self.profile.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profiles))
        
        
    def test_save_method(self):
        profile =Profiles.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profiles.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def tearDown(self):
        Images.objects.all().delete()
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.user= User(username='pip',email='go@gmail.com', password='pip2')
        self.user.save()

        self.profile=Profiles(image='/posts',bio='TGOD',user=self.user)
        self.profile.save()
        
        self.image = Images(image='posts/',caption='testing1',pub_date='16/11/2019',profile=self.user,posted=auto_now())
        self.image.save_image()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Images))

    def test_save_image(self):
        self.image.save_image()
        images= Images.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self):
        self.image.save_image()
        kwargs={'image':'/posts','caption':'dont stop me now'}
        image.update_caption(self.image.id,**kwargs)
        self.assertEqual("dont stop me now",self.image.caption)


    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Images.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_id(self):
        image_id = id
        self.image.objects.get(pk=id)
        self.assertTrue(pk=id)

    def tearDown(self):
        Images.objects.all().delete()
        
class CommentsTestClass(TestCase):


    def setup (self):
        self.user= User(username='hello',email='hello@gmail.com', password='hello123')
        self.user.save()

        self.profile=Profiles(images='/posts',bio='kenya love',user=self.user)
        self.profile.save()

        self.comment=Comments(comment='jeepers creepers',image=self.image, user=self.profile,posted=auto_now())

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        self.comment.save_comment()
        comments =Comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comments(self):
        self.comments.save_comments()
        self.comments.delete_comments()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 0)

    def tearDown(self):
        Comments.objects.all().delete()


        
        





# from django.test import TestCase
# from .models import Profile, Post
# from django.contrib.auth.models import User

# # Create your tests here.
# class TestProfile(TestCase):
#     def setUp(self):
#         self.user = User(username='scott')
#         self.user.save()

#         self.profile_test = Profile(id = 1, name='image', profile_picture='default.jpg', bio='this is a test profile', user=self.user)

#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile_test, Profile))

#     def test_save_profile(self):
#         self.profile_test.save_profile()
#         after = Profile.objects.all()
#         self.assertTrue(len(after) > 0)

#     def test_delete_profile(self):
#         self.profile_test.delete_profile()
#         after = Profile.objects.all()
#         self.assertTrue(len(after) < 1)

# class TestPost(TestCase):
#     def setUp(self):
#         self.profile_test = Profile(name='scott', user=User(username='doka'))
#         # self.profile_test.save()

#         self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

#     def test_insatance(self):
#         self.assertTrue(isinstance(self.image_test, Post))

#     def test_save_image(self):
#         self.image_test.save_image()
#         images = Post.objects.all()
#         self.assertTrue(len(images) > 0)

#     # def test_delete_image(self):
#     #     self.image_test.delete_image()
#     #     after = Post.objects.all()
#     #     self.assertTrue(len(after) < 1)
