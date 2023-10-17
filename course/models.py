from django.db import models
from users.models import Student
import uuid
import importlib


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
    student_info = models.JSONField(default=dict,blank=True)
    withdraw_status = models.BooleanField(default=False)
    
    def save(self,*args, **kwargs):
        if self._state.adding:
            self.availableChairs = self.courseChair
        
        if (self.availableChairs > 0) and (self.allowQuota_whenAvailable):
            self.quotaRecieveing_Status = True
        else:
            self.quotaRecieveing_Status = False
        super().save(*args, **kwargs)

    #testing method
    def is_chair_available(self):
        return self.availableChairs != 0
    
    #__str__
    def __str__(self):
        return f"{self.courseID}: {self.courseName} "
    

class QuotaRequest(models.Model):
    requestID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.student.name + ': ' + self.course.courseID
    


class Quota_accepeted(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    

    def save(self, *args, **kwargs):
        if self._state.adding:
            # adding a student who has been accepted
            name = str(self.student.name)
            id = str(self.student.id)
            self.course.student_info[id] = name
            # adding a course that has enrolled
            course_id = str(self.course.courseID)
            course_name = str(self.course.courseName)
            self.student.Enrolled_Course[course_id] = course_name
            self.course.availableChairs = self.course.availableChairs-1
            if (self.course.availableChairs > 0) and (self.course.allowQuota_whenAvailable):
                self.course.quotaRecieveing_Status = True
            else:
                self.course.quotaRecieveing_Status = False
            self.student.save()
            self.course.save()  # Save the related Course object here, not with *args, **kwargs

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # deleting a student name who has withdrawn
        id = str(self.student.id)
        del self.course.student_info[id]
        # deleting a course name that has been withdrawn
        course_id = str(self.course.courseID)
        del self.student.Enrolled_Course[course_id]
        
        if (self.course.availableChairs > 0) and (self.course.allowQuota_whenAvailable):
            self.course.quotaRecieveing_Status = True
        else:
            self.course.quotaRecieveing_Status = False
        self.course.availableChairs += 1
        self.student.save()
        self.course.save()  # Save the related Course object here, not with *args, **kwargs

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.courseID}"

class Quota_rejected(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='rejected_enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rejected_enrollments')

    def __str__(self):
        return f"{self.course.courseID} was rejected {self.student.name}"