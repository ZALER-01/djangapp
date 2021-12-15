from django import forms

from .models import Student
from .models import Employees

class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__"  

class studentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=100)
    lastname = forms.CharField(label="Enter last name",max_length=100)
    email =forms.EmailField(label="enter Email Address")
    file =forms.FileField()

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employees  
        fields = "__all__"  

class StudentForm1(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input  