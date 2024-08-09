from django.shortcuts import render
from django.http import HttpResponse
from.models import Department
from.models import Doctor
from .forms import BookingForm
def index(request):
    #return HttpResponse("Hello Welcome")
    
    return render(request,"index.html")
def about(request):
    #return HttpResponse("About us")
    return HttpResponse("About Us")
def dept(request):
    dic_dept={
        'dept':Department.objects.all()
    }
    return render(request,"departments.html",dic_dept)
def doctor(request):
    dic_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,"doctor.html",dic_doc)
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=BookingForm()
        dic_form={
            'form':form
        }
            
    
    form=BookingForm()
    dic_form={
        'form':form
    }
    return render(request,"booking.html",dic_form)