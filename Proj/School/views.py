from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.http import HttpResponse

from School.models import User


def studregform(request):
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        username=request.POST['u_name']
        password=request.POST['password']
        phone=request.POST['phone']
        User.objects.create_user(first_name=f_name,last_name=l_name,email=email,username=username,password=password,phone=phone,usertype="student",status=0)
        return redirect(log)
    else:
        return render(request,"studentreg.html")
        
def log(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['psw']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return render(request,"adminhome.html")
        elif user is not None and user.usertype=="student" and user.status=="1":
            login(request,user)
            request.session['studid']=user.id 
            return render(request,'studhome.html')
        elif user is not None and user.usertype=="teacher" and user.status=="1":
            login(request,user)
            request.session['teachid']=user.id 
            return render(request,'teachhome.html')
        elif user==None :
            
            
            return render(request,'login.html')
            
            
        
    else:
        return render(request,'login.html')
def registeredstudents(request):
    x=User.objects.filter(status="0")
    return render(request,"studlist.html",{'data':x})
def studapprove(request,id):
    x=User.objects.get(id=id)
    x.status="1"
    x.save()
    return redirect(registeredstudents)
    
def teacherreg(request):
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        username=request.POST['u_name']
        password=request.POST['password']
        phone=request.POST['phone']
        User.objects.create_user(first_name=f_name,last_name=l_name,email=email,username=username,password=password,phone=phone,usertype="teacher",status=1)
        return HttpResponse("Saved!!")
    else:
        return render(request,"teacherreg.html")
    
def teacherprofile(request):
    id=request.session['teachid']
    x=User.objects.get(id=id)
    return render(request,"teacherprofile.html")
    


# Create your views here.
