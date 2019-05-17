from django import forms  
from users.models import * 
class logadmin(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length = 30)