from django import forms
from .models import Movies

class updateForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['MovieName', 'MovieDescription', 'MovieYear', 'MovieImg']