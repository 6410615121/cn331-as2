from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Course, Enrollment, QuotaRequest

# Register your models here.

admin.site.register(Course)

class EnrollAdmin(admin.ModelAdmin):
    actions = ['withdraw',]

    def withdraw(self, queryset):
        for obj in queryset:
            obj.delete()
        
admin.site.register(Enrollment, EnrollAdmin)


class QuotaRequestAdmin(admin.ModelAdmin):
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'Selected quota requests approved.')

    def reject_requests(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f'Selected quota requests rejected.')

admin.site.register(QuotaRequest, QuotaRequestAdmin)



