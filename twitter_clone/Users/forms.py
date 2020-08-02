from django import forms

class ProfileForm(forms.Form):
    username=forms.CharField(label='@username',max_length=100)
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    first_name=forms.CharField(label='First Name',max_length=20)
    last_name=forms.CharField(label='Last Name',max_length=20)
    description=forms.CharField(label='Describe Yourself',widget=forms.Textarea(attrs={'rows':3, 'cols': 20}))
    profile_pic=forms.ImageField(label='Upload Profile Pic',required=False)
