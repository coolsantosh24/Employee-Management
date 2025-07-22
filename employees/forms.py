from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'salary', 'hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'})
        }