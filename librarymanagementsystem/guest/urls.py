from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/',index,name='index'),
    url(r'regerror/',TemplateView.as_view(template_name = 'registermessage.html'),name="reg"),
    url(r'logerror/',TemplateView.as_view(template_name = 'loginmessage.html'),name="log"),
    url(r'register/',registerfn,name='register'),
    url(r'login/',loginfn,name='login'),
]