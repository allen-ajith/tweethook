from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django.contrib.auth.models import User
from .models import Tweet, User
from django import forms

class TweetForm(forms.ModelForm):
    tweet = forms.CharField(label='Tweet: ',max_length=200,widget=forms.Textarea(attrs={
        "placeholder": "Your Tweet goes here",
        "rows":10,
        "cols":40
    }))
    class Meta(UserCreationForm.Meta):
        model = Tweet
        fields = ['tweet']
    
class SignUpForm(UserCreationForm):
    #name = forms.CharField(max_length=100)
    twitter_handle = forms.CharField(max_length=150)

    class Meta:
       model = User
       fields = ('username','twitter_handle','password1','password2')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User 
        fields = ('username','twitter_handle')
