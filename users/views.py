from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Student
from course.models import Course, Quota_accepeted, QuotaRequest ,Quota_rejected
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    Quotaacc  = Quota_accepeted.objects.filter(student=request.user.student)
    Quotarej  = Quota_rejected.objects.filter(student=request.user.student)
    QuotaReq =  QuotaRequest.objects.filter(student=request.user.student)
    context = {'quotaAccepted': Quotaacc,'quotaRejected':Quotarej ,'quotaRequest':QuotaReq}
    return render(request, ('users/index.html'),context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html',{
        'message': 'Logged out'
    })
        