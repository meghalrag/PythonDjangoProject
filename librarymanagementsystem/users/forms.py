from django import forms  
from users.models import * 
class Profileform(forms.Form):
    address=forms.CharField( max_length=50)
    phone=forms.IntegerField()  
    photo=forms.ImageField()