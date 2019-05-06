from django import forms  
from adminside.models import *
class loginform(forms.ModelForm):  
    class Meta:  
        fields = ('username','password')
class regform(forms.ModelForm):  
    class Meta:  
        fields = ('emailid',)
class reg(forms.ModelForm):
    class Meta:  
        model = login
        fields = ('email',)
    name=forms.CharField(max_length = 20)
    email=forms.EmailField()
    passw=forms.CharField(max_length = 100)
    cpassw=forms.CharField(max_length = 100)
class log(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length = 30)