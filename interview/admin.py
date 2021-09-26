from django.contrib import admin
from interview.models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('username', 'city', 'gender', 'first_score', 'first_result',
                    'second_score', 'second_result', 'hr_score', 'hr_result')


# Register your models here.
admin.site.register(Candidate, CandidateAdmin)
