# Generated by Django 4.2.5 on 2023-09-22 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='courseQuotaStatus',
            new_name='isQuotaAvaliable',
        ),
    ]
