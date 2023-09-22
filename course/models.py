from django.db import models

# Create your models here.
class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=64)
    courseSemester = models.IntegerField()
    courseYear = models.IntegerField()
    courseChair = models.IntegerField()
    isQuotaAvaliable = models.BooleanField(default=False)

    def __str__(self):
        return self.courseID + ': ' + self.courseName