# Generated by Django 4.2.5 on 2023-09-23 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_student_quotaaccepted_and_more'),
        ('course', '0005_enroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='stu_enroll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_en', to='users.student'),
        ),
    ]
