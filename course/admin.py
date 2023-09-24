from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Course, Enrollment, QuotaRequest
from users.models import Student

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['courseID', 'courseName', 'enrolled_students_list',]
    
admin.site.register(Course, CourseAdmin)

class EnrollAdmin(admin.ModelAdmin):
    actions = ['withdraw',]

    def withdraw(self, request, queryset):
        for obj in queryset:
            obj.delete()
        
admin.site.register(Enrollment, EnrollAdmin)


class QuotaRequestAdmin(admin.ModelAdmin):
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(approved=True)

        for obj in queryset:
            student = obj.student
            course = obj.course
            Enrollment.objects.create(student=student, course=course)
    

    def reject_requests(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f'Selected quota requests rejected.')

admin.site.register(QuotaRequest, QuotaRequestAdmin)




