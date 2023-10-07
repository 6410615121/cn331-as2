from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Quota_accepeted, QuotaRequest ,Quota_rejected
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
    student = Student.objects.get(pk=request.user)
    
    # Check if a request already exists for the student and course
    #existing_request = QuotaRequest.objects.filter(course=course, student=student)
    Quotaacc  = Quota_accepeted.objects.filter(student=request.user.student,course = course)
    Quotarej  = Quota_rejected.objects.filter(student=request.user.student,course = course)
    QuotaReq =  QuotaRequest.objects.filter(student=request.user.student,course = course)
    if Quotaacc or  Quotarej or QuotaReq:
        # A request already exists, handle the error (e.g., display a message)
        return render(request, 'quota_request_error.html')
    
    quotaObj = QuotaRequest.objects.create(course=course, student=student )
   
    return render(request, 'quota_request_success.html')

def quota_status(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    Quotaacc  = Quota_accepeted.objects.filter(student=request.user.student)
    Quotarej  = Quota_rejected.objects.filter(student=request.user.student)
    QuotaReq =  QuotaRequest.objects.filter(student=request.user.student)
    context = {'quotaAccepted': Quotaacc,'quotaRejected':Quotarej ,'quotaRequest':QuotaReq}
    return render(request, 'quota_status.html', context)
    
def quota_withdraw(request, courseID):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    course = Course.objects.get(pk=courseID)
  
    Quotaacc  = Quota_accepeted.objects.filter(student=request.user.student,course = course)
    Quotarej  = Quota_rejected.objects.filter(student=request.user.student,course = course)
    QuotaReq =  QuotaRequest.objects.filter(student=request.user.student,course = course)
    if Quotaacc :
        Quotaacc.delete()
    elif Quotarej:
        Quotarej.delete()
    elif QuotaReq:
        QuotaReq.delete()
    return render(request, 'quota_withdraw_success.html')
    