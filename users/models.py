from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return self.id + ' ' + self.name

