from django.db import models
from course.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=10,primary_key=True)

    quotaRequested = models.ManyToManyField("course.Course", related_name='quotaRequest')
    quotaAccepted = models.ManyToManyField("course.Course", related_name='quotaAccepted')
    
    def __str__(self):
        return self.id + ' ' + self.name

