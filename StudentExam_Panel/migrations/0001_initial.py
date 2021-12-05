# Generated by Django 3.2.9 on 2021-12-05 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Exam_Dashboard', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('negative_marking', models.DecimalField(decimal_places=2, max_digits=3)),
                ('timestamp', models.TimeField(auto_now_add=True)),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_result', to='Exam_Dashboard.exammodel')),
            ],
        ),
    ]
