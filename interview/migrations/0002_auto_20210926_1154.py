# Generated by Django 3.2.7 on 2021-09-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='hr_communication_ability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=16, verbose_name='坦诚沟通'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_logical_ability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=16, verbose_name='逻辑思维'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_potential',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=16, verbose_name='发展潜力'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_responsibility',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=16, verbose_name='责任心'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_result',
            field=models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=128, verbose_name='终试结果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_score',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=16, verbose_name='终试综合等级'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_stability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=16, verbose_name='稳定性'),
        ),
    ]
