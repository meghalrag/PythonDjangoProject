# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,reverse,redirect,HttpResponseRedirect
from adminside.models import *
from forms import *

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
                                                i.idbook.available=i.idbook.available-1
                                                i.idbook.save()
                                                i.save()
                                                return render(request,'messagelib.html',{'msg':'book issued successfully','username':request.session['unamelib']})
                        else:
                                obj2=issuebook.objects.all()
                                obj=register.objects.get(id=userid)
                                obj1=viewbook.objects.get(bookno=bookno)
                                for i in obj2:
                                        if i.idreg==obj and i.idbook==obj1:
                                                i.status=0
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
def logoutlib(request):
    if request.session.has_key('unamelib'):
            del request.session['idlib']
            del request.session['unamelib']
            return redirect(reverse('index'))
    else:
            return HttpResponse('you are already logged out')
