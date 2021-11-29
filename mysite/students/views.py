from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Students
from django.contrib import messages
from django.contrib.auth.models import auth,User


# Create your views here.
def home(request):
    return render(request,'index.html')


# Create your views here.
def demo(request):
    return render(request,'demo.html')



def confirm(request):
    if request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        ten_ma=request.POST['ten_ma']
        tw_ma=request.POST['tw_ma']
        usn=request.POST['usn']
        context={
            'fname':fname,
            'lname':lname,
            'ten_ma':ten_ma,
            'tw_ma':tw_ma,
            'usn':usn
        }
        return render(request,'info.html',context)
    else:
        return render(request, 'index.html')
    return render(request,'index.html')

def dataSave(request):
    if request.method == "POST":

        fname = request.POST['fname']
        lname = request.POST['lname']
        usn = request.POST['usn']
        ten_ma = request.POST['ten_ma']
        tw_ma = request.POST['tw_ma']

        sample = Students(fname=fname, lname = lname, usn = usn, ten_ma =ten_ma, tw_ma =tw_ma )
        sample.save()        
        messages.success(request,"Your data has been saved!!!")
        return redirect('home')
    else:
        messages.error(request,"Your data not saved!!!")
        return render(request, 'index.html')
 
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["username"]

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request, "invalid username or password")
            return redirect('home')
def backbtn(request):
    return render(request, 'index.html')