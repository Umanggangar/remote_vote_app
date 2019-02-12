from django import forms

from .models import User
from django.forms import ModelForm


class PostForm(forms.Form):
	CHOICES=[(1,'Narendra Modi'),(2,'Rahul Gandhi'),(3,'Sharad Pawar'),(4,'None of the Above')]
	name = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)




