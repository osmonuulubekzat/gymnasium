# Generated by Django 4.2.1 on 2023-05-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_rename_name_of_dum_mum_student_name_of_dud_mum_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Окучулар', 'verbose_name_plural': 'Окучулар'},
        ),
        migrations.AddField(
            model_name='student',
            name='image_path',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
