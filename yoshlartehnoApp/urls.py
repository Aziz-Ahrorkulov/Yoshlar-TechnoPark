from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('project/', project, name='project'),
    path('contact/', contact, name='contact'),
    path('webcam_feed/', webcam_feed, name='webcam_feed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)