# Generated by Django 3.2.9 on 2022-02-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createexam',
            name='question_amount',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
