from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from jobs.models import Job
from jobs.models import JOB_TYPES, CITIES

# Create your views here.
def job_list(request):
    job_list = Job.objects.order_by('modified_datetime')
    template = loader.get_template('joblist.html')
    context = {'job_list':job_list}

    for job in job_list:
        job.type = JOB_TYPES[job.job_type][1]
        job.city = CITIES[job.job_city][1]

    return HttpResponse(template.render(context))

def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city = CITIES[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404('Job Does not Exist.')
    
    context = {'job':job}
    template = loader.get_template('job.html')
    return HttpResponse(template.render(context))
