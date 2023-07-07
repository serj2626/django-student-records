from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm


def index(request):
    '''Стартовая страница'''
    return render(request, 'students/index.html', {'students': Student.objects.all()})


def show_student(request, id):
    '''Информация о студенте'''

    return HttpResponseRedirect(reverse('home'))


def add_student(request):
    '''Добавить нового студента'''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_number = form.cleaned_data['student_number']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            field_of_study = form.cleaned_data['field_of_study']
            gpa = form.cleaned_data['gpa']

            new_student = Student(student_number=student_number, first_name=first_name, last_name=last_name,
                                  email=email,
                                  field_of_study=field_of_study, gpa=gpa)
            new_student.save()
            return render(request, 'students/add_student.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {
        'form': form
    })


def edit(request, id):
    '''Редактирование данных студента'''

    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })


def delete(request, id):
    '''Удаление профиля студента'''

    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
