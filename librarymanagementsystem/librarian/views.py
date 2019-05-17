# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse,redirect,HttpResponseRedirect
from adminside.models import *
from forms import *
from datetime import date
from django.core.exceptions import ValidationError

# Create your views here.
def loginlib(request):
    if request.session.has_key('unamelib'):
        return render(request,'homeuserlib.html',{'username':request.session['unamelib']})
    else:
            return HttpResponse('your session is expired.please log in again')
def addbooklib(request):
        if request.session.has_key('unamelib'):
                return render(request,'addbooklib.html',{'username':request.session['unamelib']})
        else:
            return HttpResponse('your session is expired.please log in again')
def addbooklibform(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                        form=addbook(request.POST)
                        if form.is_valid():
                                bookno=form.cleaned_data['bookno']
                                bookname=form.cleaned_data['bookname']
                                author=form.cleaned_data['author']
                                quantity=form.cleaned_data['quantity']
                                obj=viewbook.objects.all()
                                for i in obj:
                                        if i.bookno==bookno:
                                                return HttpResponse('bookno already exists try another one')
                                obj=viewbook(bookno=bookno,bookname=bookname,author=author,quantity=quantity,available=quantity)
                                obj.save()
                                return render(request,'messagelib.html',{'msg':'book added successfully','username':request.session['unamelib']})
                        else:
                                return render(request,'messagelib.html',{'msg1':"failed"})        
        else:
                return HttpResponse('your session is expired.please log in again')
def viewbooklib(request):
        if request.session.has_key('unamelib'):
                obj=viewbook.objects.all()
                obj1=issuebook.objects.all()
                count=0
                for i in obj1:
                        count+=1
                if count==0:
                        for i in obj:
                                i.available=i.quantity
                                i.save()
                return render(request,'viewbooklib.html',{'obj':obj,'username':request.session['unamelib']})
        else:
            return HttpResponse('your session is expired.please log in again')

def viewbooklibform(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                        form=addbook(request.POST)
                        if form.is_valid():
                                bookno=form.cleaned_data['bookno']
                                bookname=form.cleaned_data['bookname']
                                author=form.cleaned_data['author']
                                quantity=form.cleaned_data['quantity']
                                available=request.POST['available']
                                upd=request.POST.get('update',False)
                                if upd==False:
                                        obj=viewbook.objects.get(bookno=bookno)
                                        obj.delete()
                                        return render(request,'messagelib.html',{'msg':'deleted successfully','username':request.session['unamelib']})
                                else:
                                        obj=viewbook.objects.get(bookno=bookno)
                                        return render(request,'updatebooklib.html',{'obj':obj,'username':request.session['unamelib']})
        else:
                return HttpResponse('your session is expired.please log in again')
def updatebooklibform(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                        form=updatebook(request.POST)
                        if form.is_valid():
                                bookno=form.cleaned_data['bookno']
                                bookname=form.cleaned_data['bookname']
                                author=form.cleaned_data['author']
                                quantity=form.cleaned_data['quantity']
                                available=form.cleaned_data['available']
                                obj=viewbook.objects.filter(bookno=bookno).update(bookname=bookname,author=author,
                                quantity=quantity,available=available)
                                return render(request,'messagelib.html',{'msg':'book details updated successfully','username':request.session['unamelib']})
                        else:
                                return render(request,'messagelib.html',{'msg1':"failed"})        
        else:
                return HttpResponse('your session is expired.please log in again')
def issuebooklib(request):
        if request.session.has_key('unamelib'):
                obj=issuebook.objects.all()
                return render(request,'issuebooklib.html',{'obj':obj,'username':request.session['unamelib']})
        else:
            return HttpResponse('your session is expired.please log in again')

def issuebooklibformreject(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                        bookno=request.POST['bookno']
                        userid=request.POST['userid']
                        dateto=request.POST['dateto']
                        accept=request.POST.get('accept',False)
                        obj2=issuebook.objects.all()
                        obj=register.objects.get(id=userid)
                        obj1=viewbook.objects.get(bookno=bookno)
                        for i in obj2:
                                if i.idreg==obj and i.idbook==obj1:
                                        i.dateto=dateto
                                        i.status=2
                                        i.idbook.save()
                                        try:
                                                i.save()
                                        except ValidationError:
                                                return render(request,'messagelib.html',{'msg1':'date is required','username':request.session['unamelib']})
                                        i.save()
                                        obj1.available-=1
                                        obj1.save()
                                        return render(request,'messagelib.html',{'msg':'book issued successfully','username':request.session['unamelib']})
def issuebooklibform(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                        bookno=request.POST['bookno']
                        userid=request.POST['userid']
                        dateto=request.POST['dateto']
                        accept=request.POST.get('accept',False)
                        if accept!=False:
                                obj2=issuebook.objects.all()
                                obj=register.objects.get(id=userid)
                                obj1=viewbook.objects.get(bookno=bookno)
                                for i in obj2:
                                        if i.idreg==obj and i.idbook==obj1:
                                                i.dateto=dateto
                                                i.status=2
                                                i.idbook.save()
                                                try:
                                                        i.save()
                                                except ValidationError:
                                                        return render(request,'messagelib.html',{'msg1':'date is required','username':request.session['unamelib']})
                                                return render(request,'messagelib.html',{'msg':'book issued successfully','username':request.session['unamelib']})
                        else:
                                obj2=issuebook.objects.all()
                                obj=register.objects.get(id=userid)
                                obj1=viewbook.objects.get(bookno=bookno)
                                for i in obj2:
                                        if i.idreg==obj and i.idbook==obj1:
                                                i.status=0
                                                obj1.available+=1
                                                obj1.save()
                                                i.save()
                                                return render(request,'messagelib.html',{'msg':'request rejected successfully','username':request.session['unamelib']})
                # return HttpResponse(obj2.datefrom)
                return render(request,'messagelib.html',{'msg1':'error occured','username':request.session['unamelib']})
        else:
            return HttpResponse('your session is expired.please log in again')
def rejectedbooklib(request):
        if request.session.has_key('unamelib'):
                obj=issuebook.objects.all()
                return render(request,'rejectedbooklib.html',{'obj':obj,'username':request.session['unamelib']})
        else:
            return HttpResponse('your session is expired.please log in again')
def pendingbooklib(request):
        if request.session.has_key('unamelib'):
                obj=issuebook.objects.all()
                return render(request,'pendingbooklib.html',{'obj':obj,'username':request.session['unamelib']})
        else:
            return HttpResponse('your session is expired.please log in again')
def returnbooklib1(request):
    if request.session.has_key('unamelib'):
        return render(request,'returnbooklib1.html',{'username':request.session['unamelib']})
    else:
            return HttpResponse('your session is expired.please log in again')
def returnbooklib1form(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                                form=returnclass(request.POST)
                                if form.is_valid():
                                        uname=form.cleaned_data['uname']
                                        try:
                                                obj=register.objects.get(name=uname)
                                                obj=issuebook.objects.filter(idreg=obj)
                                                return render(request,'returnbooklib2.html',{'obj':obj,'username':request.session['unamelib']})
                                        except Exception:
                                                return render(request,'messagelib.html',{'msg1':"no user found"})
                                else:
                                        return render(request,'messagelib.html',{'msg1':"form validation failed"})        
        else:
                return HttpResponse('your session is expired.please log in again')
def returnbooklib2form(request):
        if request.session.has_key('unamelib'):
                if request.method=="POST":
                        bookno=request.POST['bookno']
                        bookname=request.POST['bookname']
                        username=request.POST['username']
                        userid=request.POST['userid']
                        datefrom=request.POST['datefrom']
                        dateto=request.POST['dateto']
                        s=str(datefrom)
                        ss=s.split(' ')
                        mmf=ss[0]
                        sss=ss[1].split(',')
                        ddf=sss[0]
                        yyf=ss[2]
                        s=str(dateto)
                        ss=s.split(' ')
                        mm=ss[0]
                        sss=ss[1].split(',')
                        dd=sss[0]
                        yy=ss[2]
                        returndate=request.POST['returndate']
                        s=str(returndate)
                        ss=s.split('-')
                        yyr=ss[0]
                        mmr=ss[1]
                        ddr=ss[2]
                        mlist=['January','February','march','april','May','June','July','Augest','September','October','November','December']
                        count=0
                        for i in mlist:
                                count+=1
                                if i==mm:
                                        mm=count
                        dd=int(dd)
                        yy=int(yy)
                        ddr=int(ddr)
                        mmr=int(mmr)
                        yyr=int(yyr)
                        d0=date(yy,mm,dd)
                        d1=date(yyr,mmr,ddr)
                        duration=d1-d0
                        day=str(duration).split(' ')
                        ddnew=int(day[0])
                        if ddnew>0:
                                amt=5*ddnew
                                dur=str(ddnew)+' day is pending'
                        else:
                                amt=0
                                count=0
                                for i in mlist:
                                        count+=1
                                        if i==mmf:
                                                mmf=count
                                duration=date(yyr,mmr,ddr)-date(int(yyf),mmf,int(ddf))
                                dur=str(duration)+' days'
                                # return HttpResponse(dd+str(mm)+yy+yyr+mmr+ddr)  
                        li=[]
                        li.append(bookno)
                        li.append(userid)
                        li.append(bookname)
                        li.append(username)
                        li.append(datefrom)
                        li.append(dateto)
                        li.append(returndate)
                        li.append(amt)
                        li.append(dur)
                        # return HttpResponse(amt)  
                        return render(request,'returnbooklib3.html',{'li':li,'username':request.session['unamelib']})
        else:
                return HttpResponse('your session is expired.please log in again')
def returnbooklib3form(request):
        return HttpResponse('ok')
def logoutlib(request):
    if request.session.has_key('unamelib'):
            del request.session['idlib']
            del request.session['unamelib']
            return redirect(reverse('index'))
    else:
            return HttpResponse('you are already logged out')
