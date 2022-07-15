from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from twitterblog.models import UserProfile,Blogs




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[

            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"

        ]

class LogInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        exclude=["user",]
        widgets={
            "DOB":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }

class PostForm(ModelForm):
    class Meta:
        model=Blogs
        fields=[
            "description",
            "image"
        ]

        widgets={
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }


