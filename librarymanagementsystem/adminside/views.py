# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse,redirect,HttpResponseRedirect
from adminside.models import *
from forms import logadmin
# Create your views here.
def homefun(request):
    if request.session.has_key('unamead'):
        uname=request.session['unamead']
        return render(request,'homeuseradmin.html',{'username':uname})
    else:
        return HttpResponse('you are already logged out')
def addlib(request):
    if request.session.has_key('unamead'):
        return render(request,'addlibrarian.html',{'username':request.session['unamead']})
    else:
        return HttpResponse('you are already logged out')
def addlibform(request):
    if request.session.has_key('unamead'):
        if request.method=='POST':
            form=logadmin(request.POST)
            if form.is_valid():
                uname=form.cleaned_data['email']
                passw=form.cleaned_data['password']
                obj=login.objects.all()
                for i in obj:
                    if i.email==uname:
                        return HttpResponse('already exists')
                obj=login(email=uname,password=passw,status=2)
                obj.save()
                return render(request,'messageadmin.html',{'username':request.session['uname'],'msg':'successfull'})
    else:
        return HttpResponse('you are already logged out')


def addadmin(request):
    if request.session.has_key('unamead'):
        return render(request,'addadmin.html',{'username':request.session['unamead']})
    else:
        return HttpResponse('you are already logged out')
def addadminform(request):
    if request.session.has_key('unamead'):
        if request.method=='POST':
            form=logadmin(request.POST)
            if form.is_valid():
                uname=form.cleaned_data['email']
                passw=form.cleaned_data['password']
                obj=login.objects.all()
                for i in obj:
                    if i.email==uname:
                        return HttpResponse('already exists')
                obj=login(email=uname,password=passw,status=3)
                obj.save()
                return render(request,'messageadmin.html',{'username':request.session['uname'],'msg':'new admin created successfully'})
    else:
        return HttpResponse('you are already logged out')

def viewlib(request):
    if request.session.has_key('unamead'):
        obj=login.objects.all()
        return render(request,'viewlibrarian.html',{'username':request.session['unamead'],'obj':obj})
    else:
        return HttpResponse('you are already logged out')

def dellibform(request):
    if request.session.has_key('unamead'):
        if request.method=='POST':
            uname=request.POST['email']
            obj=login.objects.get(email=uname)
            obj.delete()
            obj=login.objects.all()
            return render(request,'viewlibrarian.html',{'username':request.session['unamead'],'obj':obj})
    else:
        return HttpResponse('you are already logged out')

def viewusers(request):
    if request.session.has_key('unamead'):
        obj=login.objects.all()
        return render(request,'viewusers.html',{'username':request.session['unamead'],'obj':obj})
    else:
        return HttpResponse('you are already logged out')
def viewadmin(request):
    if request.session.has_key('unamead'):
        obj=login.objects.all()
        return render(request,'viewadmin.html',{'username':request.session['unamead'],'obj':obj})
    else:
        return HttpResponse('you are already logged out')
def delusersform(request):
    if request.session.has_key('unamead'):
        if request.method=='POST':
            uname=request.POST['email']
            obj=login.objects.get(email=uname)
            obj.delete()
            return render(request,'messageadmin.html',{'username':request.session['unamead'],'msg':'deleted successfully'})
    else:
        return HttpResponse('you are already logged out')
def logout(request):
    if request.session.has_key('unamead'):
        del request.session['idad']
        del request.session['unamead']
        return redirect(reverse('index'))
    else:
        return HttpResponse('you are already logged out')