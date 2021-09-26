from django.contrib import admin
from interview.models import Candidate


class CandidateAdmin(admin.ModelAdmin):

    exclude = ('creator', 'created_date', 'modified_date')

    list_display = ('username', 'city', 'gender', 'first_score', 'first_result',
                    'second_score', 'second_result', 'hr_score', 'hr_result')

    list_filter = ('city', 'first_result', 'second_result', 'hr_result',
                   'first_interviewer', 'second_interviewer', 'hr_interviewer')
    search_fields = ('username', 'phone', 'email', 'bachelor_school')

    fieldsets = (
        ('基本信息', {'fields': (('username', 'gender'), ('city', 'born_address'), ('phone', 'email'), ('apply_position',  'candidate_remark'),
                             ('major', 'degree'), 'bachelor_school', 'master_school', 'doctor_school', ('test_score_of_general_ability', 'paper_score'))}),
        ('初试', {'fields': ('first_score', 'first_learning_ability', 'first_professional_competency', 'first_advantage',
         'first_disadvantage', 'first_result', 'first_recommend_position', 'first_remark', 'first_interviewer')}),
        ('复试', {'fields': ('second_score', 'second_learning_ability', 'second_professional_competency', 'second_pursue_of_excellence', 'second_communication_ability',
         'second_pressure_score', 'second_advantage', 'second_disadvantage', 'second_result', 'second_recommend_position', 'second_remark', 'second_interviewer')}),
        ('终试', {'fields': ('hr_score', 'hr_responsibility', 'hr_communication_ability', 'hr_logical_ability',
         'hr_potential', 'hr_stability', 'hr_advantage', 'hr_disadvantage', 'hr_result', 'hr_remark', 'hr_interviewer',)}),
    )


# Register your models here.
admin.site.register(Candidate, CandidateAdmin)
