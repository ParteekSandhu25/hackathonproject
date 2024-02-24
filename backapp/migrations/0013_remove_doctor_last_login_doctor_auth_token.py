# Generated by Django 5.0.2 on 2024-02-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0012_doctor_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='last_login',
        ),
        migrations.AddField(
            model_name='doctor',
            name='auth_token',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]