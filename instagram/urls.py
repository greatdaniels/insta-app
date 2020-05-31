from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url('^$', views.welcome, name = 'welcome'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name = 'index'),
]