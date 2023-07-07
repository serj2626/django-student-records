from django.urls import path
from students import views

urlpatterns = [

    path('', views.index, name='home'),
    path('<int:id>/', views.show_student, name='show-student'),
    path('add/', views.add_student, name='add-student'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
