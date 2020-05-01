import django_filters
from .models import MedicalHistory


class PatientFilter(django_filters.FilterSet):

    class Meta:
        model = MedicalHistory
        fields = ('illness',)
        labels = {
            'illness': 'Choose any illness to filter by',
        }
