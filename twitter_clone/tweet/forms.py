from django import forms

class CreateTweet(forms.Form):
    message=forms.CharField(label='',widget=forms.Textarea(attrs={'rows':3, 'cols': 20}))
