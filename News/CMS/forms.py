from django import forms
from .models import News

class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['id', 'category', 'headline','image', 'content', 'views']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)