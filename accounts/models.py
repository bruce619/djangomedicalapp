from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Choice Selection for Users Gender
SEX_TYPE = (
    ('male', 'Male'),
    ('male', 'Female')
)


#  Profile Model: Will be saved the the database
class Profile(models.Model):
    # Columns for Profile Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(choices=SEX_TYPE, null=True, blank=True, max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)
    profession = models.CharField(null=True, blank=True, max_length=40)
    address = models.CharField(null=True, blank=True, max_length=50)
    phone_number = models.CharField(null=True, blank=True, max_length=20)
    Nationality = models.CharField(null=True, blank=True, max_length=20)
    next_of_kin = models.CharField(null=True, blank=True, max_length=40)
    next_of_kin_phone_number = models.CharField(null=True, blank=True, max_length=20)
    next_of_kin_address = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        #  Return the username on the database "e.g Dean Profile"
        return f'{self.user.username} Profile'

    # Saves a users profile
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)




