# Generated by Django 3.2.9 on 2022-02-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Dashboard', '0004_alter_viewanssheet_all_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewanssheet',
            name='all_question',
            field=models.TextField(blank=True, max_length=100000, null=True),
        ),
    ]