# Generated by Django 4.2.5 on 2023-09-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_alter_course_availablechairs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='availableChairs',
            field=models.IntegerField(default=0),
        ),
    ]
