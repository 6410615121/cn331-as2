# Generated by Django 4.2.5 on 2023-09-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_remove_course_courseno_remove_course_id_and_more'),
        ('users', '0003_remove_student_quotacourse_student_quotaaccept_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='quotaAccepttest',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]
