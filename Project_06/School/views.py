from django.shortcuts import render
from School.models import Student,Studmark,User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def sign_in(request):
    if request.method=="POST":
        n=request.POST['name']
        a=request.POST['age']
        Student.objects.create(name=n,age=a)
        return HttpResponse('saved!!!')
    else:
        return render(request,'register.html')
def studmark(request):
    if request.method=="POST":
        s=request.POST['sid']
        m=request.POST['mark']
        g=request.POST['grade']
        Studmark.objects.create(stdid_id=s,mark=m,grade=g)
        return HttpResponse("saved!!@")
        
    else:
        x=Student.objects.all()
        return render(request,"studmark.html",{'data':x})
    
def studmarkview(request):
    x=Studmark.objects.all()
    return render(request,'mark.html',{'data':x})

def registerstudent(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        em=request.POST['email']
        un=request.POST['uname']
        pw=request.POST['psw']
        pl=request.POST['place']
        ph=request.POST['phone']
        User.objects.create_user(first_name=fn,last_name=ln,username=un,email=em,password=pw,place=pl,phone=ph,usertype="student",status=0)
        return HttpResponse("saved!!@")
        
    else:
        x=User.objects.all()
        return render(request,"registerform.html",{'data':x})
    
