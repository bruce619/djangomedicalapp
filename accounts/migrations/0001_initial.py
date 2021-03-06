# Generated by Django 2.2 on 2020-05-01 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('male', 'Female')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profession', models.CharField(blank=True, max_length=40, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=20, null=True)),
                ('next_of_kin', models.CharField(blank=True, max_length=40, null=True)),
                ('next_of_kin_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('next_of_kin_address', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
