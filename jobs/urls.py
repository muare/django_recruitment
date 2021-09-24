from django.urls import path
from . import views

urlpatterns = [
    path('joblist/', views.job_list, name='joblist'),
    path('job/<int:job_id>', views.job_detail, name='job_detail')
]
