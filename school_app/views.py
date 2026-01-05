from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, this is my_app home page!")
    data = {"name":"Coca"}
    return  render(request,"index.html",context=data)

def find_by_id(request,id):
    return HttpResponse(f"Id{id}")

def content(request):
    return render(request,"pages/main_content.html")
# Create your views here.