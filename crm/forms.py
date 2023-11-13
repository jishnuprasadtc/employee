from django import forms
from crm.models import Employees

from django.contrib.auth.models import User

class EmployeeForms(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    contact=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
 
class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"

        widgets={

            "name":forms.TextInput(attrs={"class":"form-control "}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "contact":forms.Textarea(attrs={"class":"form-control","rows":5})

        }

        
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})

        }


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    # created beacuse ordinary form due to we want to checks if that exist in database



