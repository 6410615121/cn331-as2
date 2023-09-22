from django.db import models

# Create your models here.
class Course(models.Model):
    courseNo = models.CharField(max_length=10)
    courseName = models.CharField(max_length=64)
    courseSemester = models.IntegerField()
    courseYear = models.IntegerField()
    courseChair = models.IntegerField()
    isQuotaAvaliable = models.BooleanField(default=False)

    def __str__(self):
        return self.courseNo + ': ' + self.courseName