from django.contrib import admin
from jobs.models import Job


class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_datetime', 'modified_datetime')
    list_display = ('job_title', 'job_type', 'job_city', 'creator',
                    'created_datetime', 'modified_datetime')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Job, JobAdmin)