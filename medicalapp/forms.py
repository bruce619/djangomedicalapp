from django import forms
from .models import MedicalHistory


class MedicalHistoryForm(forms.ModelForm):

    class Meta:
        model = MedicalHistory
        fields = ('illness', 'symptoms', 'additional_info', 'disability', 'medications',)
        exclude = ('user', 'created_at',)
        labels = {
            'illness': 'Select a Medical Illness if you have any',
            'symptoms': 'What are the Symptoms you are experiencing',
            'additional_info': 'Additional Info',
            'disability': 'Do you have any Disability?',
            'medications': 'Are you on any Medications?',

        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
