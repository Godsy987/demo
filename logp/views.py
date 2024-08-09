from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Register
from django.urls import reverse
from django.contrib import messages

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=Register.objects.filter(username=username,password=password).first()
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('signin')
        else:
            request.session['uname']=username
            return redirect('Home')
    return render(request,'signin.html')
def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        myreg=Register(name=name,phone=phone,email=email,username=username,password=password)
        myreg.save()
        return redirect('signin')
    return render(request,"register.html")
def logout(request):
    if 'uname' not in request.session:
        request.session.flush()
        return redirect('signin')
def index(request):
    if 'uname' not in request.session:
        return redirect('signin')
    return render(request,"indexview.html")
def logout(request):
    return render(request,"index.html")
def viewall(request):
    if 'uname' not in request.session:
        return redirect('signin')
    reg=Register.objects.all()
    context={
        'reg':reg,
    }
    return render(request,"viewreg.html",context)
def updatereg(request,pk):
    reg=Register.objects.get(id=pk)
    dic={
        'reg':reg,
    }
    return render(request,"update.html",dic)
def updatedata(request,pk):
    name=request.POST["name"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    username=request.POST["username"]
    password=request.POST["password"]
    reg = Register.objects.get(id=pk)
    reg.name = name
    reg.phone = phone
    reg.email = email
    reg.username = username
    reg.password = password
    reg.save()
    return HttpResponseRedirect(reverse('viewall'))
def deletereg(request,pk):
    reg = Register.objects.get(id=pk)
    reg.delete()
    return HttpResponseRedirect(reverse('viewall'))

