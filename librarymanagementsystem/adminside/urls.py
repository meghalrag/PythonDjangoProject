from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView,ListView
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'adminhome/',homefun,name='adminhome'),
    url(r'adminaddlibrarian/',addlib,name='adminaddlibrarian'),
    url(r'adminaddadmin/',addadmin,name='adminaddadmin'),
    url(r'adminviewlibrarian/',viewlib,name='adminviewlibrarian'),
    url(r'adminviewusers/',viewusers,name='adminviewusers'),
    url(r'adminviewadmin/',viewadmin,name='adminviewadmin'),
    url(r'deletelibrarianform/',dellibform,name='deletelibrarianform'),
    url(r'deleteusersform/',delusersform,name='deleteusersform'),
    url(r'adminaddlibrarianform/',addlibform,name='adminaddlibrarianform'),
    url(r'adminaddadminform/',addadminform,name='adminaddadminform'),
    url(r'logoutadmin/',logout,name='logoutadmin'),

]