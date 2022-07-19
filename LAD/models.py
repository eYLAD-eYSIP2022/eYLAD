# from cProfile import label
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class DiscourseAPI(models.Model):
    name = models.CharField(max_length=50)
    url = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "DiscourseAPI"


class Theme(models.Model):
    theme = models.CharField(max_length=10, help_text="Please, enter abbrevations like \'AB\', \'SS\'")

    def __str__(self):
        return str(self.theme)

    class Meta:
        ordering = ('theme',)


class LADUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    theme = models.CharField(choices = [(x, x) for x in Theme.objects.all().values_list('theme', flat=True)] , max_length = 100)

    def __str__(self):
        return str(self.user) + "-" + str(self.theme)


class SignUpForm(UserCreationForm):
    theme = forms.ChoiceField(choices = [(x, x) for x in Theme.objects.all().values_list('theme', flat=True)])

    class Meta:
        model = User
        fields = ('username', 'theme', 'password1', 'password2')

