# forms.py
from django import forms
from .models import Prediction

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        exclude = ['user','risk']  # Exclude the 'risk' field from the form

    # Add custom widgets and labels for better presentation
    gender = forms.ChoiceField(choices=Prediction.GENDER_CHOICES, widget=forms.RadioSelect, label='Gender')
    smoking_status = forms.ChoiceField(choices=Prediction.SMOKING_STATUS_CHOICES, widget=forms.RadioSelect, label='Smoking Status')

