# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class login(models.Model):
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField( max_length=50)
    status=models.IntegerField()

class register(models.Model):
    name=models.CharField( max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    phone=models.IntegerField(null=True)
    photo=models.ImageField(upload_to='profilepic',null=True)
    fkidlog=models.ForeignKey(login,on_delete=models.CASCADE)
class viewbook(models.Model):
    bookno=models.CharField(max_length=50)
    bookname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    quantity=models.IntegerField()
    available=models.IntegerField()
class issuebook(models.Model):
    idreg=models.ForeignKey(register,on_delete=models.CASCADE)
    idbook=models.ForeignKey(viewbook,on_delete=models.CASCADE)
    datefrom=models.DateField(auto_now_add=True,null=True)
    dateto=models.DateField(null=True)
    status=models.IntegerField()
class payment(models.Model):
    idpayreg=models.ForeignKey(register, on_delete=models.CASCADE)
    idissue=models.ForeignKey(issuebook, on_delete=models.CASCADE)
    amount=models.IntegerField()





