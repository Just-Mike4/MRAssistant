from django import forms
from.models import MoodData
class MoodForm(forms.ModelForm):
    class Meta:
        model=MoodData
        fields=['moodmatrix','description']