from django.shortcuts import render,redirect
from firstapp.forms import userform

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from firstapp.models import User
from jobpostapp.models import add_job,subscribe
from jobpostapp.forms import sub



# Create your views here.
@login_required(login_url="login")

def home(request):
    sonu=add_job.objects.all().order_by("-view_count")[0:3]
    so=add_job.objects.all().order_by("-view_count")[0:1]
    son=add_job.objects.all().order_by("-Time")[0:3]
    a=subscribe.objects.all()
    b = sub()
    saved = False
    if request.method =='POST':
        b=sub(request.POST) 
        if b.is_valid():
            b.save()
            saved =True
            print("subscribed sucessfulley")
    return render(request,"home.html",{'sonu':sonu,'a':a,'b':b,'saved':saved,'so':so,'son':son})


def registrstion(request):
    registered = False
    if request.method == 'POST':
        form = userform(request.POST)
        # profileform = form2(request.POST,request.FILES)

        if form.is_valid() :
            print("saved sucessfulley")
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            registered = True
    else:
        form = userform()
        # profileform = form2()
    return render(request,'register.html',{'form':form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('pls check the cred....!!')
    return render(request,'login.html',{})

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")


def user_profile(request):
    # user = User.objects.all()
    return render(request,"profile.html")




    
    