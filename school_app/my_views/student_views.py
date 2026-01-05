from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from school_app.models import Student


def index(request):
    if request.method == "POST":
        search_item = request.POST.get('search_item', '')
        students = Student.objects.filter(first_name__icontains=search_item) | Student.objects.filter(last_name__icontains=search_item)
    else:
        students = Student.objects.all()

    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"students": page_obj}
    return render(request, "pages/students/index.html", data)


def show(request):
    return render(request, "pages/students/create.html")


def create(request):
    if request.method == "POST":
        student = Student(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            gender=request.POST['gender'],
            dob=request.POST['dob'],
            address=request.POST['address']
        )
        student.full_clean()
        student.save()
        messages.success(request, "Student created successfully")
        return redirect("/students/index")
    return render(request, "pages/students/create.html")


def delete(request, id):
    try:
        student = Student.objects.get(pk=id)
        student.delete()
        messages.success(request, "Student deleted successfully")
    except ObjectDoesNotExist:
        messages.error(request, "Student not found")
    return redirect("/students/index")


def edit(request, id):
    try:
        student = Student.objects.get(pk=id)
        data = {"student": student}
        return render(request, "pages/students/edit.html", data)
    except ObjectDoesNotExist:
        messages.error(request, "Student not found")
        return redirect("/students/index")


def update(request, id):
    try:
        student = Student.objects.get(pk=id)
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.gender = request.POST['gender']
        student.dob = request.POST['dob']
        student.address = request.POST['address']
        student.full_clean()
        student.save()
        messages.success(request, "Student updated successfully")
        return redirect("/students/index")
    except ObjectDoesNotExist:
        messages.error(request, "Student not found")
        return redirect("/students/index")
