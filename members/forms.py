from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpFrom(UserCreationForm):
        email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
        first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
        last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Secnod name'}))
  
   
        class Meta:
          model = User
          fields = ('username','first_name','last_name','email','password1','password2')

        def __init__(self,*args,**kwargs):
           super(SignUpFrom, self).__init__(*args, **kwargs)    
           self.fields['username'].widget.attrs['class'] = 'form-control'
           self.fields['username'].widget.attrs['placeholder'] = 'Username'
           self.fields['password1'].widget.attrs['class'] = 'form-control'
           self.fields['password1'].widget.attrs['placeholder'] = 'Password'
           self.fields['password2'].widget.attrs['class'] = 'form-control'  
           self.fields['password2'].widget.attrs['placeholder'] = 'Conform Password'  