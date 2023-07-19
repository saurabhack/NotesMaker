from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import AddNotes
from .forms import MyForm
# Create your views here.
def index(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user!=None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credential invalid')
            return redirect('/')
    else:
        at=AddNotes.objects.all()    
        return render(request,'index.html',{'at':at})
def regiser(request):
    if request.method=='POST':
        username=request.POST['username']
        age=request.POST['age']
        clas=request.POST['clas']
        email=request.POST['email']
        subject=request.POST['subjects']
        password=request.POST['password1']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.infor(request,'username is already used')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect(regiser)
        else:
            messages.info(request,'password does not matched')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
from django.shortcuts import redirect

def AddNote(request):
    if request.method == 'POST':
        forms = MyForm(request.POST)
        if forms.is_valid():
            forms.save()
            return  redirect('/')
    else:
        forms = MyForm()
        return render(request, 'AddNote.html',{'forms':forms})
 
