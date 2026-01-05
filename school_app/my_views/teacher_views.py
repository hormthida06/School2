from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from school_app.models import Teacher

def index(request):
    if request.method == "POST":
        search_item = request.POST.get('search_item', '')
        teachers = Teacher.objects.filter(first_name__icontains=search_item) | Teacher.objects.filter(last_name__icontains=search_item)
    else:
        teachers = Teacher.objects.all()

    paginator = Paginator(teachers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"teachers": page_obj}
    return render(request, "pages/teachers/index.html", data)


def show(request):
    return render(request, "pages/teachers/create.html")


def create(request):
    if request.method == "POST":
        teacher = Teacher(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            gender=request.POST['gender'],
            dob=request.POST['dob'],
            address=request.POST['address'],
            salary = request.POST['salary']
        )
        teacher.full_clean()
        teacher.save()
        messages.success(request, "Teacher created successfully")
        return redirect("/teachers/index")
    return render(request, "pages/teachers/create.html")


def delete(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
        messages.success(request, "Teacher deleted successfully")
    except ObjectDoesNotExist:
        messages.error(request, "Teacher not found")
    return redirect("/teachers/index")


def edit(request, id):
    try:
        teacher = Teacher.objects.get(pk=id)
        data = {"teacher": teacher}
        return render(request, "pages/teachers/edit.html", data)
    except ObjectDoesNotExist:
        messages.error(request, "Teacher not found")
        return redirect("/teachers/index")


def update(request, id):
        teacher_existing = Teacher.objects.get(pk=id)
        teacher_existing.first_name = request.POST['first_name']
        teacher_existing.last_name = request.POST['last_name']
        teacher_existing.gender = request.POST['gender']
        teacher_existing.dob = request.POST['dob']
        teacher_existing.address = request.POST['address']
        teacher_existing.salary = request.POST['salary']
        teacher_existing.full_clean()
        teacher_existing.save()
        messages.success(request, "Teacher updated successfully")
        return redirect("/teachers/edit/{id}")



