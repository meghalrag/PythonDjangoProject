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
    url(r'issuebooklibformreject/',issuebooklibformreject,name="issuebooklibformreject"),
    url(r'rejectedbooklib/',rejectedbooklib,name="rejectedbooklib"),
    url(r'pendingbooklib/',pendingbooklib,name="pendingbooklib"),
    url(r'returnbooklib1/',returnbooklib1,name="returnbooklib1"),
    url(r'returnbooklib1form/',returnbooklib1form,name="returnbooklib1form"),
    url(r'returnbooklib2form/',returnbooklib2form,name="returnbooklib2form"),
    url(r'returnbooklib3form/',returnbooklib3form,name="returnbooklib3form"),
    url(r'logoutlib/',logoutlib,name="logoutlib"),
]