from django.db import models

# Create your models here.
DEGREES = [('学士', '学士'), ('硕士', '硕士'), ('博士', '博士')]
FIRST_INTERVIEW_RESULTS = [('建议复试', '建议复试'), ('待定', '待定'), ('放弃', '放弃')]
SECOND_INTERVIEW_RESULTS = [('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')]
FINAL_INTERVIEW_RESULTS = [('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')]
HR_SCORES = [('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')]
GENDERS=[('男','男'),('女','女')]

class Candidate(models.Model):
    # basic info
    # userid = models.IntegerField(
    #     unique=True, blank=True, null=True, verbose_name='应聘者ID')
    username = models.CharField(max_length=128, verbose_name='姓名')
    city = models.CharField(max_length=128, verbose_name='城市')
    phone = models.CharField(max_length=128, verbose_name='电话号码')
    email = models.EmailField(max_length=128, blank=True, verbose_name='邮箱')
    apply_position = models.CharField(
        max_length=128, blank=True, verbose_name='应聘职位')
    born_address = models.CharField(
        max_length=128, blank=True, verbose_name='生源地')
    gender = models.CharField(max_length=128, choices=GENDERS, blank=True, verbose_name='性别')
    candidate_remark = models.CharField(
        max_length=128, blank=True, verbose_name='候选人备注')

    creator = models.CharField(
        max_length=128, blank=True, verbose_name='创建人')
    last_editor = models.CharField(
        max_length=128, blank=True, verbose_name='最后编辑者')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    bachelor_school = models.CharField(
        max_length=128, blank=True, verbose_name='学士学校')
    master_school = models.CharField(
        max_length=128, blank=True, verbose_name='硕士学校')
    doctor_school = models.CharField(
        max_length=128, blank=True, verbose_name='博士学校')
    major = models.CharField(max_length=128, blank=True, verbose_name='专业')
    degree = models.CharField(
        max_length=128, choices=DEGREES, blank=True, verbose_name='学历')

    # exams
    test_score_of_general_ability = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='综合能力测评成绩')
    paper_score = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='笔试成绩')

    # first round of test
    first_score = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='初试分数')
    first_learning_ability = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='学习能力得分')
    first_professional_competency = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='专业能力得分')
    first_advantage = models.TextField(
        max_length=1024, blank=True, verbose_name='优势')
    first_disadvantage = models.TextField(
        max_length=1024, blank=True, verbose_name='顾虑和不足')
    first_result = models.CharField(
        max_length=128, choices=FIRST_INTERVIEW_RESULTS, blank=True, verbose_name='初试结果')
    first_recommend_position = models.CharField(
        max_length=128, blank=True, verbose_name='推荐部门')
    first_remark = models.CharField(
        max_length=128, blank=True, verbose_name='初试备注')
    first_interviewer = models.CharField(
        max_length=128, blank=True, verbose_name='初试面试官')

    # second round of test
    second_score = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='复试分数')
    second_learning_ability = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='学习能力得分')
    second_professional_competency = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='专业能力得分')
    second_pursue_of_excellence = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='追求卓越得分')
    second_communication_ability = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='沟通能力得分')
    second_pressure_score = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, verbose_name='抗压能力得分')
    second_advantage = models.TextField(
        max_length=1024, blank=True, verbose_name='优势')
    second_disadvantage = models.TextField(
        max_length=1024, blank=True, verbose_name='顾虑和不足')
    second_result = models.CharField(
        max_length=128, choices=SECOND_INTERVIEW_RESULTS, blank=True, verbose_name='复试结果')
    second_recommend_position = models.CharField(
        max_length=128, blank=True, verbose_name='推荐部门')
    second_remark = models.CharField(
        max_length=128, blank=True, verbose_name='复试备注')
    second_interviewer = models.CharField(
        max_length=128, blank=True, verbose_name='复试面试官')

    # hr round of test
    hr_score = models.CharField(
        max_length=16, choices=HR_SCORES, blank=True, verbose_name='终试综合等级')
    hr_responsibility = models.CharField(
        max_length=16, choices=HR_SCORES, blank=True, verbose_name='责任心')
    hr_communication_ability = models.CharField(
        max_length=16, choices=HR_SCORES, blank=True, verbose_name='坦诚沟通')
    hr_logical_ability = models.CharField(
        max_length=16, choices=HR_SCORES, blank=True, verbose_name='逻辑思维')
    hr_potential = models.CharField(
        max_length=16, choices=HR_SCORES, blank=True, verbose_name='发展潜力')
    hr_stability = models.CharField(
        max_length=16, choices=HR_SCORES, blank=True, verbose_name='稳定性')
    hr_advantage = models.TextField(
        max_length=1024, blank=True, verbose_name='优势')
    hr_disadvantage = models.TextField(
        max_length=1024, blank=True, verbose_name='顾虑和不足')
    hr_result = models.CharField(
        max_length=128, choices=FINAL_INTERVIEW_RESULTS, blank=True, verbose_name='终试结果')
    hr_remark = models.CharField(
        max_length=128, blank=True, verbose_name='终试备注')
    hr_interviewer = models.CharField(
        max_length=128, blank=True, verbose_name='终试面试官')

    class Meta:
        verbose_name = '应聘者'
        verbose_name_plural = '应聘者'

    def __str__(self):
        return self.username
