# Generated by Django 4.2.5 on 2023-09-24 10:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_delete_quotaall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='availableChairs',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='quotarequest',
            name='requestID',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
