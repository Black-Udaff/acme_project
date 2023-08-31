from django import forms

from .models import Birthday
from .validators import real_age

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}
