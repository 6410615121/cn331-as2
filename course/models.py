from django.db import models
from users.models import Student
# Create your models here.
class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=64)
    courseSemester = models.IntegerField()
    courseYear = models.IntegerField()
    courseChair = models.IntegerField(default=0)

    availableChairs = models.IntegerField(default = 0)
    allowQuota_whenAvailable = models.BooleanField(default=False)
    quotaRecieveing_Status = models.BooleanField(default=False ,editable=False)

    def save(self):
        if not self.pk: 
            self.availableChairs = self.courseChair
        return super.save()
    
    def __str__(self):
        return self.courseID + ': ' + self.courseName
    
class QuotaRequest(models.Model):
    requestID = models.CharField(max_length=10, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name + ': ' + self.course.courseID


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def save(self): #new enrollment
        if not self.pk:
            self.course.availableChairs -= 1

        if (self.availableChairs > 0) and (self.allowQuota_whenAvailable):
            self.course.quotaRecieveing_Status = True
        return super.save(self)
    
    def delete(self): #new enrollment
        self.course.availableChairs += 1
        return super.delete(self)
    

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.courseID}"

