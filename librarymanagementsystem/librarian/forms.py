from django import forms 
class addbook(forms.Form):
    bookno=forms.CharField()
    bookname=forms.CharField(max_length=50)
    author=forms.CharField(max_length=50)
    quantity=forms.IntegerField()
class updatebook(forms.Form):
    bookno=forms.CharField()
    bookname=forms.CharField(max_length=50)
    author=forms.CharField(max_length=50)
    quantity=forms.IntegerField()
    available=forms.IntegerField()
class returnclass(forms.Form):
    uname=forms.CharField(max_length=50) 