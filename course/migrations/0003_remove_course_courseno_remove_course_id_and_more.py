# Generated by Django 4.2.5 on 2023-09-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_coursequotastatus_course_isquotaavaliable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseNo',
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AddField(
            model_name='course',
            name='courseID',
            field=models.CharField(default=0, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
