from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.view_student, name="view_student"),
    path('añadir/', views.add, name='añadir'),
    path('editar/<int:id>/', views.edit, name='editar'),
    path('delete/<int:id>/', views.delete, name='delete'),
]