# Generated by Django 4.2.5 on 2023-09-24 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_enroll_coursename'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Enroll',
        ),
    ]
