from django.db import models
from django.conf import settings

JOB_TYPES = [
    (0, '技术类'),
    (1, '内容类'),
    (2, '营销类'),
    (3, '运营类'),
    (4, '设计类'),
    (5, '产品类'),
]

CITIES = [
    (0, '北京'),
    (1, '上海'),
    (2, '广州'),
    (3, '深圳'),
    (4, '杭州'),
    (5, '成都'),
]


# Create your models here.
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False,
                                        choices=JOB_TYPES,
                                        verbose_name='职位类别')
    job_title = models.CharField(max_length=250,
                                 blank=False,
                                 verbose_name='职位名称')
    job_city = models.SmallIntegerField(blank=False,
                                        choices=CITIES,
                                        verbose_name='工作地点')
    job_description = models.TextField(max_length=1024,
                                       blank=False,
                                       verbose_name='工作职责')
    job_requirement = models.TextField(max_length=1024,
                                       blank=False,
                                       verbose_name='工作要求')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.SET_NULL)
    created_datetime = models.DateTimeField(auto_now_add=True,
                                            verbose_name='创建时间')
    modified_datetime = models.DateTimeField(auto_now=True,
                                             verbose_name='修改时间')
