from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_number", 
            "first_name", 
            "last_name", 
            "email", 
            "field_of_student",
            "gpa"
        ]
        
        labels = {
            "student_number": "Nº Studiante",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Email",
            "field_of_student": "Asignatura",
            "gpa": "GPA",
        }

        widgets = {
            "student_number": forms.NumberInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "field_of_student": forms.TextInput(attrs={"class": "form-control"}),
            "gpa": forms.NumberInput(attrs={"class": "form-control"})
        }