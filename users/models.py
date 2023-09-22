from django.db import models
from course.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=10,primary_key=True)

    quotaRequest = models.ManyToManyField("course.Course", related_name='quotaRequest')
    quotaAccept = models.ManyToManyField("course.Course", related_name='quotaAccept')
    
    def __str__(self):
        return self.id + ' ' + self.name

