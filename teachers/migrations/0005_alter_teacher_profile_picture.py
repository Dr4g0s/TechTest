# Generated by Django 3.2.5 on 2021-07-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_alter_teacherdata_csv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(default='default_image.jpg', upload_to='teachers/'),
        ),
    ]
