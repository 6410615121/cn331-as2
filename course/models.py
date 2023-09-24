from django.db import models
from users.models import Student
import uuid

# Create your models here.
class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=64)
    courseSemester = models.IntegerField()
    courseYear = models.IntegerField()
    courseChair = models.IntegerField(default=0)

    availableChairs = models.IntegerField(default=0, editable=False)
    allowQuota_whenAvailable = models.BooleanField(default=False)
    quotaRecieveing_Status = models.BooleanField(default=True ,editable=False)

    def enrolled_students_list(self):
        return ', '.join([enrollment.student.name for enrollment in self.enrollments.all()])

    def save(self):
        self.availableChairs = self.courseChair
        if (self.availableChairs > 0) and (self.allowQuota_whenAvailable):
            self.quotaRecieveing_Status = True
        else:
            self.quotaRecieveing_Status = False
        super().save()
    
    def __str__(self):
        return f"{self.courseID}: {self.courseName}"
    

class QuotaRequest(models.Model):
    requestID = models.UUIDField(max_length=10, primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name + ': ' + self.course.courseID
    
#class Quota(models.Model):
 #   course = models.ForeignKey(Course, on_delete=models.CASCADE)
#    student = models.ForeignKey(Student, on_delete=models.CASCADE)
#    QuotaRequest = models.ForeignKey(QuotaRequest, on_delete=models.CASCADE)

    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    def save(self): #new enrollment
        if self._state.adding:
            self.course.availableChairs -= 1

        if (self.course.availableChairs > 0) and (self.course.allowQuota_whenAvailable):
            self.course.quotaRecieveing_Status = True
        else:
            self.quotaRecieveing_Status = False

        self.course.save()
        super().save()
    
    def delete(self):
        self.course.availableChairs += 1
        
        if (self.course.availableChairs > 0) and (self.course.allowQuota_whenAvailable):
            self.course.quotaRecieveing_Status = True
        else:
            self.quotaRecieveing_Status = False
        self.course.save()

        super().delete()
        
    

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.courseID}"
    
