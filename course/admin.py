from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Course, Quota_accepeted, QuotaRequest ,Quota_rejected
from users.models import Student

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['courseID', 'courseName','availableChairs' ]
    readonly_fields = ('student_info',)
admin.site.register(Course,CourseAdmin)

class Quota_accepetedAdmin(admin.ModelAdmin):
    list_display = ['course','student' ]
    actions = ['withdraw',]

    def withdraw(self, request, queryset):
        print("withdraw method called") # show when testing
        for obj in queryset:
            obj.delete()
        
admin.site.register(Quota_accepeted, Quota_accepetedAdmin)


class QuotaRequestAdmin(admin.ModelAdmin):
    list_display = ['course','student','requestID' ]
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        for obj in queryset:
            student = obj.student
            course = obj.course
            Quota_accepeted.objects.create(student=student, course=course)   
            obj.delete()
    

    def reject_requests(self, request, queryset):
        for obj in queryset:
            student = obj.student
            course = obj.course
            Quota_rejected.objects.create(student=student, course=course)
            obj.delete()
        self.message_user(request, f'Selected quota requests rejected.')
    
    

admin.site.register(QuotaRequest, QuotaRequestAdmin)
class Quota_rejectedAdmin(admin.ModelAdmin):
    list_display = ['course','student' ]

admin.site.register(Quota_rejected,Quota_rejectedAdmin)



