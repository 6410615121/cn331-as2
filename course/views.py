from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course

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



def requestQuota(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    

