# Generated by Django 3.2.9 on 2021-12-18 22:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('UUID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuesionModel_Three',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Exam_Dashboard.basemodel')),
                ('Q_Description', models.TextField(blank=True, max_length=5000, null=True)),
                ('Q_one', models.TextField(blank=True, max_length=5000, null=True)),
                ('Q_image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('sample_one', models.CharField(blank=True, max_length=400, null=True)),
                ('sample_two', models.CharField(blank=True, max_length=400, null=True)),
                ('sample_three', models.CharField(blank=True, max_length=400, null=True)),
                ('marks', models.IntegerField(default=5)),
            ],
            bases=('Exam_Dashboard.basemodel',),
        ),
        migrations.CreateModel(
            name='QuestionModel_One',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Exam_Dashboard.basemodel')),
                ('question_name', models.TextField(max_length=4000, unique=True)),
                ('q_image', models.ImageField(blank=True, null=True, upload_to='Question_img')),
                ('marks', models.IntegerField(default=5)),
            ],
            bases=('Exam_Dashboard.basemodel',),
        ),
        migrations.CreateModel(
            name='QuestionModel_Two',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Exam_Dashboard.basemodel')),
                ('description', models.TextField(blank=True, max_length=4000, null=True)),
                ('Q_name', models.TextField(blank=True, max_length=4000, null=True)),
                ('Q_image', models.ImageField(upload_to='Question_img')),
                ('marks', models.IntegerField(default=5)),
            ],
            bases=('Exam_Dashboard.basemodel',),
        ),
        migrations.CreateModel(
            name='AnswerMode_One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.CharField(max_length=3000)),
                ('is_correct', models.BooleanField(default=False)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question', to='Exam_Dashboard.questionmodel_one')),
            ],
        ),
        migrations.CreateModel(
            name='AnsModel_Two',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Exam_Dashboard.basemodel')),
                ('ans', models.CharField(max_length=400)),
                ('is_correct', models.BooleanField(default=False)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_two', to='Exam_Dashboard.questionmodel_two')),
            ],
            bases=('Exam_Dashboard.basemodel',),
        ),
        migrations.CreateModel(
            name='AnsModel_Three',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Exam_Dashboard.basemodel')),
                ('ans', models.CharField(max_length=400)),
                ('is_correct', models.BooleanField(default=False)),
                ('Question_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_three', to='Exam_Dashboard.quesionmodel_three')),
            ],
            bases=('Exam_Dashboard.basemodel',),
        ),
    ]
