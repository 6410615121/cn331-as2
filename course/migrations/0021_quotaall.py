# Generated by Django 4.2.5 on 2023-09-24 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_alter_enrollment_course_alter_enrollment_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotaAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotaRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QuotaAll', to='course.quotarequest')),
            ],
        ),
    ]
