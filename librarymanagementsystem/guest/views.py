# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse,redirect,HttpResponseRedirect
from forms import reg,log
from adminside.models import login,register
# Create your views here.
def index(request):
    # return HttpResponse('ok')
    return render(request,'index123.html',{})
def registerfn(request):
    if request.method=="POST":
        ff=reg(request.POST)
        if ff.is_valid():
            name=ff.cleaned_data['name']
            email=ff.cleaned_data['email']
            passw=ff.cleaned_data['passw']
            cpassw=ff.cleaned_data['cpassw']
            obj=login(email=email,password=passw,status=1)
            obj.save()
            obj=login.objects.get(email=email)
            obj1=register(name=name,fkidlog=obj)
            obj1.save()
            # return HttpResponse(name)
            return render(request,'message.html',{'msg':'successfully registered'})
        else:
            # return render(request,'register.html',{})
            return HttpResponseRedirect('guest/regerror/#popup4')
def loginfn(request):
    flag=0
    if request.method=="POST":
        ff=log(request.POST)
        if ff.is_valid():
            email=ff.cleaned_data['email']
            password=ff.cleaned_data['password']
            obj=login.objects.all()
            for i in obj:
                if i.email==email and i.password==password:
                    flag=1
                    if i.status==1:
                        if request.session.has_key('unameuser'):
                            return redirect(reverse('homeuser'))
                        else:
                            request.session['iduser']=i.id
                            request.session['unameuser']=email
                            return redirect(reverse('homeuser'))
                    if i.status==2:
                        if request.session.has_key('unamelib'):
                            return redirect(reverse('homelib'))
                        else:
                            request.session['idlib']=i.id
                            request.session['unamelib']=email
                            return redirect(reverse('homelib'))
                    if i.status==3:
                        request.session['idad']=i.id
                        request.session['unamead']=email
                        return redirect(reverse('adminhome'))
            if flag==0:
                return HttpResponseRedirect('guest/logerror/#popup3')
                # return render(request,'index.html',{})
        else:
            # return render(request,'register.html',{})
            return HttpResponseRedirect('guest/logerror/#popup3')