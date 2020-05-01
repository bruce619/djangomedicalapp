from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

ILLNESS_CHOICES = (
    ("Anxiety", "Anxiety"),
    ("Arthritis", "Arthritis"),
    ("Asthma", "Asthma"),
    ("Anemia", "Anemia"),
    ("Cancer", "Cancer"),
    ("Corona_virus", "Corona Virus"),
    ("Diabetes", "Diabetes"),
    ("Ebola", "Ebola"),
    ("HIV", "HIV"),
)


class MedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    illness = models.CharField(choices=ILLNESS_CHOICES, max_length=50)
    symptoms = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=100)
    disability = models.BooleanField(default=False)
    medications = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} Medical History'







