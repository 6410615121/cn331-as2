# Generated by Django 4.2.5 on 2023-09-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_student_valid_student_coursenumber'),
        ('course', '0028_alter_quotarequest_requestid'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='names_student',
            field=models.ManyToManyField(to='users.student'),
        ),
    ]