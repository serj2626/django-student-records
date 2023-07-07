from django.db import models


class Student(models.Model):
    student_number = models.PositiveIntegerField(verbose_name='Номер студента')
    first_name = models.CharField(max_length=50, verbose_name='Имя студента')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия студента')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    field_of_study = models.CharField(max_length=50, verbose_name='Предмет')
    gpa = models.FloatField(verbose_name='Средний балл')

    def __str__(self):
        return f'''Студент {self.first_name} {self.last_name}'''

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('-gpa',)
