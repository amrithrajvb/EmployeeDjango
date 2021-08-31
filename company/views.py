from django.shortcuts import render,redirect
from company.models import Employee
from company import forms


# Create your views here.

def employeeadd(request):
    form=forms.EmployeeAddForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.EmployeeAddForm(request.POST)
        if form.is_valid():
            # emp_name=form.cleaned_data["emp_name"]
            # department=form.cleaned_data["department"]
            # salary=form.cleaned_data["salary"]
            # experience=form.cleaned_data["experience"]
            # emp=Employee(emp_name=emp_name,department=department,salary=salary,experience=experience)
            # emp.save()
            form.save()
            return render(request,'add_employee.html',context)
        else:
            return render(request, 'add_employee.html', {"form": form})
    return render(request,'add_employee.html',context)


def employeeview(request):
    form=forms.SearchEmpForm()
    emp=Employee.objects.all()
    context={}
    context["emp"]=emp
    context["form"] = form
    if request.method=="POST":
        form=forms.SearchEmpForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data["emp_name"]
            emps=Employee.objects.filter(emp_name__contains=emp_name)|Employee.objects.filter(department__contains=emp_name)
            context["emp"]=emps
            return render(request, 'employeeview.html', context)
    return render(request,'employeeview.html',context)

def employeedetails(request,id):
    emp=Employee.objects.get(id=id)
    context={"emp":emp}
    return render(request,"employeedetail.html",context)

def employeeremove(request,id):
    emp=Employee.objects.get(id=id)
    # emp_name=Employee.objects.filter(id=emp.id)
    # print(emp_name)
    emp.delete()
    return redirect('employeeview')

def employeechange(request,id):
    emp=Employee.objects.get(id=id)
    # data={
    #     "emp_name":emp.emp_name,
    #     "department":emp.department,
    #     "salary":emp.salary,
    #     "experience":emp.experience
    # }
    form=forms.EmployeeChange(instance=emp)
    context = {"form": form}
    if request.method=="POST":
        form=forms.EmployeeChange(request.POST,instance=emp)
        if form.is_valid():
            # emp_name=form.cleaned_data["emp_name"]
            # department=form.cleaned_data["department"]
            # salary=form.cleaned_data["salary"]
            # experience=form.cleaned_data["experience"]
            # emp.emp_name=emp_name
            # emp.department=department
            # emp.salary=salary
            # emp.experience=experience
            # emp.save()
            form.save()
            return redirect('employeeview')

    return render(request,"test.html",context)




