# Generated by Django 3.2.5 on 2021-07-16 01:50

from django.db import migrations, models
import teachers.models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subjects_taught',
            field=models.CharField(blank=True, help_text='Enter subjects separated by comma (,)', max_length=255, null=True, validators=[teachers.models.restrict_amount]),
        ),
    ]