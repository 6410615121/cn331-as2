from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Student(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    Enrolled_Course = models.JSONField(default=dict,blank=True)

    def __str__(self):
        return f"{self.id} : {self.name} "