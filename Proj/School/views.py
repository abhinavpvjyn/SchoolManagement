from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout 
from School.models import User

def log(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['psw']
        user=authenticate(request,username=u,password=p)
        print(user)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return render(request,"adminhome.html")
            
        
    else:
        return render(request,'login.html')

# Create your views here.
