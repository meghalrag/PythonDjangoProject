# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse,redirect,HttpResponseRedirect
from adminside.models import *
from forms import *

# Create your views here.
def homeuser(request):
        if request.session.has_key('unameuser'):
                uname=request.session['unameuser']
                obj=register.objects.get(fkidlog=request.session['iduser'])
                return render(request,'index.html',{'obj':obj})
        else:
                return HttpResponse('you are already logged out')
    
def aboutuser(request):

        if request.session.has_key('unameuser'):
                return render(request,'about.html',{})
        else:
                return HttpResponse('you are already logged out')
def galleryuser(request):
        if request.session.has_key('unameuser'):
                return render(request,'about.html',{})
        else:
                return HttpResponse('you are already logged out')
def editprofileuser(request):
        if request.session.has_key('unameuser'):
                return render(request,'editprofuser.html',{})
        else:
                return HttpResponse('you are already logged out')
def editprofileuserform(request):
        if request.session.has_key('unameuser'):
                if request.method=='POST':
                        form=Profileform(request.POST, request.FILES)
                        if form.is_valid():  
                                address=form.cleaned_data["address"]
                                phone=form.cleaned_data["phone"]
                                proname=form.cleaned_data["photo"]
                                obj=register.objects.get(fkidlog=request.session['iduser'])
                                if obj.address==None:
                                        obj.address=address
                                        obj.phone=phone
                                        obj.photo=proname
                                        obj.save()
                                        # return HttpResponse(obj.fkidlog.id)
                                        return render(request,'messageuser.html',{'obj':obj,'msg':'Profile updated successfully'})
                                else:
                                        return render(request,'messageuser.html',{'obj':obj,'msg1':'Error occured...You are already updated Profile.'})
                        else:
                                return render(request,'messageuser.html',{'obj':obj,'msg2':'form validation failed'})
        else:
                return HttpResponse('you are already logged out')
def searchbookuser(request):
        if request.session.has_key('unameuser'):
                if request.method=="POST":
                        searchname=request.POST['bookname']
                obj=viewbook.objects.all()
                for i in obj:
                        if i.bookname==searchname:
                                return render(request,'searchbookuser.html',{'i':i,'username':request.session['unameuser']})
                return render(request,'viewbookuser.html',{'obj':obj,'msg':'no result found','username':request.session['unameuser']})                
        else:
            return HttpResponse('your session is expired.please log in again')
def viewbookuser(request):
        if request.session.has_key('unameuser'):
                obj=viewbook.objects.all()
                return render(request,'viewbookuser.html',{'obj':obj,'username':request.session['unameuser']})
        else:
            return HttpResponse('your session is expired.please log in again')
def viewbookuserform(request):
        if request.session.has_key('unameuser'):
                if request.method=="POST":
                        bookno=request.POST['bookno']
                        obj=register.objects.get(fkidlog=request.session['iduser'])
                        obj1=viewbook.objects.get(bookno=bookno)
                        if obj.phone==None:
                                return render(request,'index.html',{'obj':obj})
                        elif obj1.available==0:
                                return render(request,'messageuser.html',{'msg1':'sorry!!!book is unavailable'})
                        else:
                                obj2=issuebook.objects.all()
                                for i in obj2:
                                        if i.idreg==obj and i.idbook==obj1:
                                                if i.status==0:
                                                        return HttpResponse('u cannot request this book')
                                                if i.status!=3:
                                                        return HttpResponse('u r already requested')
                                                
                                obj2=issuebook(idreg=obj,idbook=obj1,status=1)
                                obj2.save()
                                obj1.available-=1
                                obj1.save()
                                # return HttpResponse(obj2.datefrom)
                                return render(request,'messageuser.html',{'msg':'Your request submiited wait to accept librarian','username':request.session['unameuser']})
        else:
            return HttpResponse('your session is expired.please log in again')
def requestedbookuser(request):
        if request.session.has_key('unameuser'):
                obj1=register.objects.get(fkidlog=request.session['iduser'])
                obj=issuebook.objects.filter(idreg=obj1)
                return render(request,'requestedbookuser.html',{'obj':obj,'username':request.session['unameuser']})
        else:
            return HttpResponse('your session is expired.please log in again')
def pendingbookuser(request):
        if request.session.has_key('unameuser'):
                obj1=register.objects.get(fkidlog=request.session['iduser'])
                obj=issuebook.objects.filter(idreg=obj1)
                return render(request,'pendingbookuser.html',{'obj':obj,'username':request.session['unameuser']})
        else:
            return HttpResponse('your session is expired.please log in again')
def logoutuser(request):
        if request.session.has_key('unameuser'):
                del request.session['iduser']
                del request.session['unameuser']
                return redirect(reverse('index'))
        else:
                return HttpResponse('you are already logged out')