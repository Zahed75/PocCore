# Generated by Django 3.2.9 on 2022-02-02 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Exam_Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(blank=True, max_length=500, null=True)),
                ('negative_marking', models.CharField(blank=True, max_length=40)),
                ('timestamp', models.CharField(blank=True, max_length=50, null=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_result', to='Exam_Dashboard.createexam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllStudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(blank=True, max_length=400, null=True)),
                ('name', models.CharField(blank=True, max_length=550, null=True)),
                ('board', models.CharField(blank=True, max_length=550, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=550, null=True)),
                ('score', models.CharField(blank=True, max_length=550, null=True)),
                ('negative_marking', models.CharField(blank=True, max_length=550, null=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam_Dashboard.createexam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
