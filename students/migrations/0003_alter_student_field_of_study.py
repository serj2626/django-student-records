# Generated by Django 3.2.13 on 2023-06-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='field_of_study',
            field=models.CharField(max_length=50, verbose_name='Предмет'),
        ),
    ]
