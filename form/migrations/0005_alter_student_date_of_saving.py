# Generated by Django 4.2.1 on 2023-05-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_student_date_of_saving'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_saving',
            field=models.DateTimeField(blank=True, default='2023-05-27 14:28:19', verbose_name=''),
        ),
    ]
