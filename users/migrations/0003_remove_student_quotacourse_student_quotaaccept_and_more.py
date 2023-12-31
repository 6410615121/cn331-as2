# Generated by Django 4.2.5 on 2023-09-22 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_course_courseno_remove_course_id_and_more'),
        ('users', '0002_student_quotacourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='quotaCourse',
        ),
        migrations.AddField(
            model_name='student',
            name='quotaAccept',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='quotaAccept', to='course.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='quotaRequest',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='quotaRequest', to='course.course'),
        ),
    ]
