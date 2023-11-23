from ast import arg
from django import forms 
from .models import Account
from django.contrib.auth.password_validation import validate_password
from django.core import validators 


class RegistrationForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password must contain 8 character, 2 digits and 1 uppercase letter.'  }))

     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'  }))

     class Meta: 
       model = Account 
       fields = [ 'first_name', 'last_name', 'phone_number', 'email', 'password']

     def _init_(self,*args, **kwargs):
        super(RegistrationForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

     def clean(self):
         cleaned_data = super(RegistrationForm, self).clean()
         password = cleaned_data.get('password')
         if len(password)<8:
          raise forms.ValidationError('Your password must contain at least 8 characters.')
         if sum(c.isdigit() for c in password) < 2:
          raise forms.ValidationError('Password must container at least 2 digits.')
         if not any(c.isupper() for c in password):
          raise forms.ValidationError('Password must container at least 1 uppercase letter.')
         confirm_password = cleaned_data.get('confirm_password')

         if password != confirm_password:
             raise forms.ValidationError("Password doesnot match")