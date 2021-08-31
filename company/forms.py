from django import forms
from django.forms import ModelForm
from company.models import Employee
import re
class EmployeeAddForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        widgets={
            "emp_name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.TextInput(attrs={"class":"form-control"}),
            "experience":forms.TextInput(attrs={"class":"form-control"})
        }

        labels={
            "emp_name":"Employee Name"
        }
    # emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # salary=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    # experience=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        emp_name=cleaned_data["emp_name"]
        salary=cleaned_data["salary"]
        department=cleaned_data["department"]
        experience=cleaned_data["experience"]
        x="[a-zA-Z]*"
        if int(salary)<0:
            msg="invalid salary"
            self.add_error("salary",msg)

        if int(experience)<0:
            msg="invalid experience"
            self.add_error("experience",msg)
        matcher=re.fullmatch(x,emp_name)
        if matcher is not None:
            pass
        else:
            msg="please enter valid employee name"
            self.add_error("emp_name",msg)

        depmatcher = re.fullmatch(x, department)
        if depmatcher is not None:
            pass
        else:
            msg = "please enter valid department name"
            self.add_error("department", msg)

class EmployeeChange(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
        widgets={
            "emp_name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.TextInput(attrs={"class":"form-control"}),
            "experience":forms.TextInput(attrs={"class":"form-control"})
        }

        labels={
            "emp_name":"Employee Name"
        }
    # emp_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # department = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # salary = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    # experience = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data=super().clean()
        salary = cleaned_data["salary"]
        experience = cleaned_data["experience"]

        if int(salary) < 0:
            msg="invalid price"
            self.add_error("salary",msg)
        if int(experience) < 0:
            msg="invalid experience"
            self.add_error("experience",msg)

class SearchEmpForm(forms.Form):
    emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


