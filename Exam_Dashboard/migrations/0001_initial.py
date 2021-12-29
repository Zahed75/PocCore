# Generated by Django 3.2.9 on 2021-12-29 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamPack_name', models.CharField(max_length=1000, verbose_name='Exam Pack Name')),
                ('pack_image', models.ImageField(blank=True, null=True, upload_to='pack_image')),
                ('details', models.TextField()),
                ('batch', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question_model_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('option_one', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_one_is_correct', models.BooleanField(default=False)),
                ('option_two', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_two_is_correct', models.BooleanField(default=False)),
                ('option_three', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_three_is_correct', models.BooleanField(default=False)),
                ('option_four', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_four_is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question_model_three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('one_question', models.CharField(blank=True, max_length=1000, null=True)),
                ('one_image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('one_option_one', models.CharField(blank=True, max_length=1000, null=True)),
                ('one_option_one_is_correct', models.BooleanField(default=False)),
                ('one_option_two', models.CharField(blank=True, max_length=1000, null=True)),
                ('one_option_two_is_correct', models.BooleanField(default=False)),
                ('one_option_three', models.CharField(blank=True, max_length=1000, null=True)),
                ('one_option_three_is_correct', models.BooleanField(default=False)),
                ('one_option_four', models.CharField(blank=True, max_length=1000, null=True)),
                ('one_option_four_is_correct', models.BooleanField(default=False)),
                ('two_question', models.CharField(blank=True, max_length=3000, null=True)),
                ('two_image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('two_data_one', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_data_two', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_data_three', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_option_one', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_option_one_is_correct', models.BooleanField(default=False)),
                ('two_option_two', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_option_two_is_correct', models.BooleanField(default=False)),
                ('two_option_three', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_option_three_is_correct', models.BooleanField(default=False)),
                ('two_option_four', models.CharField(blank=True, max_length=1000, null=True)),
                ('two_option_four_is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question_model_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('data_one', models.CharField(blank=True, max_length=2000, null=True)),
                ('data_two', models.CharField(blank=True, max_length=2000, null=True)),
                ('data_three', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_one', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_one_is_correct', models.BooleanField(default=False)),
                ('option_two', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_two_is_correct', models.BooleanField(default=False)),
                ('option_three', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_three_is_correct', models.BooleanField(default=False)),
                ('option_four', models.CharField(blank=True, max_length=2000, null=True)),
                ('option_four_is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CreateExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.CharField(blank=True, max_length=40)),
                ('Exam_name', models.CharField(max_length=1000)),
                ('details', models.TextField()),
                ('Exam_start_time', models.TimeField()),
                ('Exam_start_date', models.DateField()),
                ('Exam_end_time', models.TimeField()),
                ('Exam_end_date', models.DateField()),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='exam_cover_photos')),
                ('level', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=100)),
                ('total_mark', models.IntegerField(default=0)),
                ('pass_mark', models.IntegerField(default=0)),
                ('mark_per_question', models.IntegerField(default=1)),
                ('isRandomized', models.BooleanField(default=False, verbose_name='Randomization')),
                ('isSorted', models.BooleanField(default=False, verbose_name='Sorting')),
                ('isNegativeMarking', models.BooleanField(default=False, verbose_name='Negative Marking')),
                ('amount_per_mistake', models.FloatField(default=0, verbose_name='Amount per mistake')),
                ('exam_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_pack', to='Exam_Dashboard.exampack')),
            ],
        ),
    ]
