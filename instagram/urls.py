from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name = 'index'),
    url(r'^user/(?P<username>\w+)',views.profile,name='profile'), 
    url(r'^image/(?P<image_id>\d+)',views.view_single_image,name='singleImage'),
    url(r'^accounts/edit/', views.edit_profile, name='edit_profile'),
    url(r'^postImage/',views.new_image,name='postImage'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)