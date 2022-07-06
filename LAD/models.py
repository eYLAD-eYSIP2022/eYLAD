# from cProfile import label
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Create your models here.

theme_category = (
    ("AB", "AB"),
    ("BM", "BM"),
    ("DB", "DB"),
    ("FW", "FW"),
    ("SM", "SM"),
    ("SS", "SS"),
)

class User(User):
    theme = models.CharField(choices = theme_category, max_length = 100)

class SignUpForm(UserCreationForm):
    theme = forms.ChoiceField(choices = theme_category)

    class Meta:
        model = User
        fields = ('username', 'theme', 'password1', 'password2')