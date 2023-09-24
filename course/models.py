from django.db import models
from users.models import Student

# Create your models here.
class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=64)
    courseSemester = models.IntegerField()
    courseYear = models.IntegerField()
    courseChair = models.IntegerField(default=0)

    availableChairs = models.IntegerField(default=0, editable=True)
    allowQuota_whenAvailable = models.BooleanField(default=False)
    quotaRecieveing_Status = models.BooleanField(default=False ,editable=False)

    def save(self):
        if self._state.adding: 
            self.availableChairs = self.courseChair
        super().save()
    
    def __str__(self):
        return f"{self.courseID}: {self.courseName} : {self.availableChairs}"
    
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
        if self._state.adding:
            self.course.availableChairs -= 1

        if (self.course.availableChairs > 0) and (self.course.allowQuota_whenAvailable):
            self.course.quotaRecieveing_Status = True

        self.course.save()
        super().save()
    
    def delete(self,*args, **kwargs):
        self.course.availableChairs += 1
        self.course.save(*args, **kwargs)

        super(Enrollment, self).delete(*args, **kwargs)
        
    

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.courseID}"

