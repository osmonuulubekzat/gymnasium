# Generated by Django 4.2.1 on 2023-05-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_alter_student_options_student_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_saving',
            field=models.DateTimeField(default='2023-05-27 14:27:34', verbose_name=''),
        ),
    ]
