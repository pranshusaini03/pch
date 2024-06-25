from django.http import HttpResponse
from django.shortcuts import render,redirect
from cart.models import cart
from django.http import JsonResponse
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from product.models import products
from grooming.models import dgroomer
from grooming.models import lgroomer
from grooming.models import mgroomer
from grooming.models import kgroomer
from grooming.models import bgroomer
from grooming.models import hgroomer
from health.models import ddoctor
from health.models import ldoctor
from health.models import mdoctor
from health.models import bdoctor
from health.models import kdoctor
from health.models import hdoctor
from adoption.models import dadopt
from adoption.models import kadopt
from adoption.models import badopt
from adoption.models import ladopt
from adoption.models import madopt
from adoption.models import hadopt
from form.models import form
from django.contrib import messages
from django.contrib.auth import authenticate
from form.models import healthform
from form.models import groomingform

def save_form(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        pettype=request.POST.get('pettype')
        message=request.POST.get('message')
        en=form.objects.create(name=name,email=email,phoneno=phoneno,address=address,pettype=pettype,message=message)
        en.save()
    return render(request,"adoption.html")
def save_gform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        pettype=request.POST.get('pettype')
        date=request.POST.get('date')
        time=request.POST.get('time')
        en=groomingform.objects.create(name=name,email=email,phoneno=phoneno,address=address,pettype=pettype,date=date,time=time)
        en.save()
    return render(request,"grooming.html")

def save_hform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        pettype=request.POST.get('pettype')
        date=request.POST.get('date')
        time=request.POST.get('time')
        message=request.POST.get('message')
        en=healthform.objects.create(name=name,email=email,phoneno=phoneno,address=address,pettype=pettype,date=date,time=time,message=message)
        en.save()
    return render(request,"health.html")

def save_cart(request):
    if request.method=="POST":
        image=request.POST.get('image')
        name=request.POST.get('name')
        price=request.POST.get('price')
        message=request.POST.get('message')
        en=cart.objects.create(image=image,name=name,price=price,message=message)
        en.save()
    return render(request,"home.html")
def save_cart1(request):
    dests=products.objects.all()
    if request.method=="POST":
        image=request.POST.get('image')
        name=request.POST.get('name')
        price=request.POST.get('price')
        message=request.POST.get('message')
        en=cart.objects.create(image=image,name=name,price=price,message=message)
        en.save()
    return render(request,"ps.html",{'dests':dests})
def cart1(request):
    carts=cart.objects.all()
    return render(request,"cart.html",{'carts':carts})
def vform(request):
    return render(request,"form.html")
def gform(request):
    return render(request,"gform.html")
def hform(request):
    return render(request,"hform.html")



def signin1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,"home.html",{'fname':username})
        else:
            messages.error(request,"bad crendnetial")
            return render(request,"home.html")
    return render(request,"signin.html")
def signup(request):  
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_user=fname
        myuser.last_user=lname
        myuser.save()
        messages.success(request,"Your Account has been successfully created")
        return render(request,"signin.html")
    return render(request,"signup.html")

def signout(request):
    logout(request)
    messages.success(request,"logged Out successfully")
    return render(request,"home.html")

def index(request):
        
    return render(request,"index.html")

def home(request):
        
    return render(request,"home.html")
def grooming(request):
    return render(request,"grooming.html")
def adoption(request):
    return render(request,"adoption.html")
def health(request):
    return render(request,"health.html")
def dgrooming(request):
    grooms=dgroomer.objects.all()
    return render(request,"dgrooming.html",{'grooms':grooms})
def kgrooming(request):
    grooms=kgroomer.objects.all()
    return render(request,"kgrooming.html",{'grooms':grooms})
def lgrooming(request):
    grooms=lgroomer.objects.all()
    return render(request,"lgrooming.html",{'grooms':grooms})
def mgrooming(request):
    grooms=mgroomer.objects.all()
    return render(request,"mgrooming.html",{'grooms':grooms})
def bgrooming(request):
    grooms=bgroomer.objects.all()
    return render(request,"bgrooming.html",{'grooms':grooms})
def hgrooming(request):
    grooms=hgroomer.objects.all()
    return render(request,"hgrooming.html",{'grooms':grooms})

def dadoption(request):
    docs=dadopt.objects.all()
    return render(request,"dadoption.html",{'docs':docs})
def ladoption(request):
    docs=ladopt.objects.all()
    return render(request,"ladoption.html",{'docs':docs})
def madoption(request):
    docs=madopt.objects.all()
    return render(request,"madoption.html",{'docs':docs})
def badoption(request):
    docs=badopt.objects.all()
    return render(request,"badoption.html",{'docs':docs})
def kadoption(request):
    docs=kadopt.objects.all()
    return render(request,"kadoption.html",{'docs':docs})
def hadoption(request):
    docs=hadopt.objects.all()
    return render(request,"hadoption.html",{'docs':docs})

def dhealths(request):
    adps=ddoctor.objects.all()
    return render(request,"dhealth.html",{'adps':adps})
def lhealths(request):
    adps=ldoctor.objects.all()
    return render(request,"lhealth.html",{'adps':adps})
def mhealths(request):
    adps=mdoctor.objects.all()
    return render(request,"mhealth.html",{'adps':adps})
def khealths(request):
    adps=kdoctor.objects.all()
    return render(request,"khealth.html",{'adps':adps})
def bhealths(request):
    adps=bdoctor.objects.all()
    return render(request,"bhealth.html",{'adps':adps})
def hhealths(request):
    adps=hdoctor.objects.all()
    return render(request,"hhealth.html",{'adps':adps})
def ps(request):
   dests=products.objects.all()
   return render(request,"ps.html",{'dests':dests})