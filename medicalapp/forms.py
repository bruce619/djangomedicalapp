from django import forms
from .models import MedicalHistory


class MedicalHistoryForm(forms.ModelForm):

    class Meta:
        model = MedicalHistory
        fields = ('illness', 'symptoms', 'additional_info', 'disability', 'medications',)
        exclude = ('user', 'created_at',)
        labels = {
            'illness': 'Select Illness/Illnesses you have or have been treated of',
            'symptoms': 'What Are The Symptoms You Are Experiencing. if None write "No Symptoms" ',
            'additional_info': 'Provide Other Illness/Illnesses you have or have been treated of. if None write "No Additional Information"',
            'disability': 'Do you have any Disability?',
            'medications': 'Are you on any Medications?',
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
