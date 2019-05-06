from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'homelib/',loginlib,name="homelib"),
    url(r'addbooklib/',addbooklib,name="addbooklib"),
    url(r'addbooklibform/',addbooklibform,name="addbooklibform"),
    url(r'viewbooklib/',viewbooklib,name="viewbooklib"),
    url(r'viewbooklibform/',viewbooklibform,name="viewbooklibform"),
    url(r'updatebooklibform/',updatebooklibform,name="updatebooklibform"),
    url(r'issuebooklib/',issuebooklib,name="issuebooklib"),
    url(r'issuebooklibform/',issuebooklibform,name="issuebooklibform"),
    url(r'rejectedbooklib/',rejectedbooklib,name="rejectedbooklib"),
    url(r'pendingbooklib/',pendingbooklib,name="pendingbooklib"),
    url(r'logoutlib/',logoutlib,name="logoutlib"),
]