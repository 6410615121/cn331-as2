from django.contrib import admin
from .models import Course, Enrollment, QuotaRequest

# Register your models here.

admin.site.register(Course)
admin.site.register(Enrollment)


class QuotaRequestAdmin(admin.ModelAdmin):
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'Selected quota requests approved.')

    def reject_requests(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f'Selected quota requests rejected.')

admin.site.register(QuotaRequest, QuotaRequestAdmin)



