from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib import admin
from users.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'homeuser/',homeuser,name="homeuser"),
    url(r'about/',aboutuser,name="about"),
    url(r'gallery/',galleryuser,name="gallery"),
    url(r'editprofileuser/',editprofileuser,name="editprofileuser"),
    url(r'editprofileuserform/',editprofileuserform,name="editprofileuserform"),
    url(r'searchbookuser/',searchbookuser,name="searchbookuser"),
    url(r'viewbookuser/',viewbookuser,name="viewbookuser"),
    url(r'viewbookuserform/',viewbookuserform,name="viewbookuserform"),
    url(r'requestedbookuser/',requestedbookuser,name="requestedbookuser"),
    url(r'pendingbookuser/',pendingbookuser,name="pendingbookuser"),
    url(r'logoutuser/',logoutuser,name="logoutuser"),
]