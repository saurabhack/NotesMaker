from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import AddNotes
from .forms import MyForm
from django.views.decorators.csrf import csrf_protect
# Rest of your views...



# Create your views here.
@csrf_protect
def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    else:
        at=AddNotes.objects.all()
        return render(request,'index.html',{'at':at})
@csrf_protect
def register(request):
    if request.method == 'POST':
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
                messages.info(request,'username is already used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('register')
        else:
            messages.info(request,'password does not matched')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def AddNote(request):
    if request.method == 'POST':
        forms = MyForm(request.POST)
        if forms.is_valid():
            forms.save()
            return  redirect('/')
    else:
        forms = MyForm()
        return render(request, 'AddNote.html',{'forms':forms})
def delete(request,item_id):
    item_id=AddNotes.objects.get(id=item_id)
    item_id.delete()
    return redirect('/')
def show(request,item_id):
    item=AddNotes.objects.get(id=item_id)
    return render(request,'show.html',{'item':item})

  # Replace 'YourModel' with the name of your model

def search_result(request):
    if request.method=='POST':
        query=request.POST['search']
        if query:
            results=AddNotes.objects.filter(chapter__contains=query)
            return render(request,'search_result.html',{'results':results})
        else:
            messages.info(request,'information is not available')
            return render(request,'search_result.html',{})
    return render(request,'search_result.html')

    