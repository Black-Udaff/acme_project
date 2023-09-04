from django import forms

from .models import Birthday, Congratulation


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        # fields = '__all__'
        exclude = ('author',)
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}


class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ('text',)
