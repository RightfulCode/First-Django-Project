from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee,Department,Role
from .forms import EmployeeForm

# Create your views here.

def add_page(request):
    if request.method == 'POST':
        page = EmployeeForm(request.POST)
        if page.is_valid():
            page.save()
            return redirect('/read')
    else:
        page = EmployeeForm()

    context = {
        'object':page
    }
    return render(request, 'add.html',context)

def delete_page(request):
    employee = Employee.objects.all()
    context = {
        'objects':employee
    }
    return render(request, 'delete_page.html', context)

def show_employee(request):
    employee = Employee.objects.all()
    context = {
        "objects":employee
    }
    return render(request, 'show.html', context)

def home(request):
    return render(request, 'home.html')

def delete_employee(request, id):
    member = Employee.objects.get(id=id)
    member.delete()
    return redirect('/read')

def update_page(request):
    employee = Employee.objects.all()
    context = {
        'objects':employee
    }
    return render(request, 'update.html', context)

def update_employee(request,id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('/read')
    
    context = {
        'form':form
    }
    return render(request, 'updated.html', context)