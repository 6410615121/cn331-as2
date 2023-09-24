from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, QuotaRequest
from users.models import Student

# Create your views here.
def course_list(request): #show all course, status
    courses  = Course.objects.all()
    context = {'Courses': courses}
    return render(request, 'course_list.html', context)

def course_detail(request, courseID):
    course  = Course.objects.get(pk=courseID)
    return render(request, 'course_detail.html', {
        "CourseID" : courseID,
        "CourseName": course.courseName,
        "CourseYear": course.courseYear,
        "CourseSemester": course.courseSemester,
        "CourseChair": course.courseChair,
        "chairAvailable": course.availableChairs,
        "quotaAvailable": course.quotaRecieveing_Status,
    })


def quota_request(request, courseID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    course = Course.objects.get(pk=courseID)
    student = Student.objects.get(id=request.user)
    
    # Check if a request already exists for the student and course
    existing_request = QuotaRequest.objects.filter(course=course, student=student)

    if existing_request:
        # A request already exists, handle the error (e.g., display a message)
        return render(request, 'quota_request_error.html')
    
    quotaObj = QuotaRequest.objects.create(course=course, student=student)
    return render(request, 'quota_request_success.html')

    

