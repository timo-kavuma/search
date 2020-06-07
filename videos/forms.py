from django import forms
from .models import Video

class SearchForm(forms.Form):
    query = forms.CharField()