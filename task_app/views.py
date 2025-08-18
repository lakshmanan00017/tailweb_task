from django.shortcuts import render,redirect
from .models import teacher, studends,AuditLog
from .form import markform,loginform,registerform 
import hashlib, os
from django.contrib import messages
from .session import *
from django.utils import timezone

def home(request):
    token = request.COOKIES.get("session_token")
    teacher_id = validate_session(token)
    if not teacher_id:
        return redirect("login_page")
    data=studends.objects.all()
    return render(request,"home.html",{"data":data})

def login_page(request):
    form=loginform()
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            salt= 'test'
            hash_password=hashlib.sha256((salt + password).encode()).hexdigest()
            
            try:
                user=teacher.objects.filter(username=username).first()
                if user and user.password == hash_password:
                    token = create_session(user.id)
                    response = redirect('home')
                    response.set_cookie(
                        key="session_token",
                        value=token,
                        httponly=True,
                        secure=False, 
                        samesite="Strict"
                    )
                    return response
                messages.error(request,"password is wrong")
                return render(request,"login.html" ,{"form":form})
                
            except teacher.DoesNotExist:
                return render(request,"login.html" ,{"form":form})
            
    return render(request,"login.html" ,{"form":form})

def calculate_new_mark(new,old):
    new_mark=new+old
    if new_mark > 100:
        return 0
    return new_mark

def add_student(request):
    token = request.COOKIES.get("session_token")
    teacher_id = validate_session(token)
    if not teacher_id:
        return redirect("login_page")
    form=markform()
    if request.method=="POST":
        form=markform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            subject=form.cleaned_data['subject']
            mark=form.cleaned_data['mark']
            data=studends.objects.filter(name=name)
            for i in data:
                if name == i.name and subject== i.subject:
                    new_mark=calculate_new_mark(mark,i.mark)
                    if new_mark == 0:
                        messages.error(request,'Your total mark is greater then 100.')
                        return redirect('home')
                    studends.objects.filter(id=i.id).update(mark=new_mark)
                    messages.success(request, "Marks updated successfully!")
                    return redirect('home')
            form.save()
            messages.success(request, "successfully added new Record")
            return redirect('home')

    return render(request,"add_student.html",{'form':form})
def register(request):
    form=registerform()
    if request.method=="POST":
        form=registerform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            salt= 'test'
            hash_password=hashlib.sha256((salt + password).encode()).hexdigest()

            teacher.objects.create(username=username,password=hash_password)

            return redirect('login_page')
            
    return render(request,"register.html",{'form':form})

def logout_page(request):
    
    token = request.COOKIES.get("session_token")
    destroy_session(token)
    response = redirect("login_page")
    response.delete_cookie("session_token")
    return response
    
def update(request,id):
    token = request.COOKIES.get("session_token")
    teacher_id = validate_session(token)
    if not teacher_id:
        return redirect("login_page")
    mark=studends.objects.get(id=id)
    form=markform(instance=mark)
    if request.method=='POST':
        form=markform(request.POST,instance=mark)
        if form.is_valid():
            form.save()
            new_mark=form.cleaned_data['mark']
            AuditLog.objects.create(teacher_id=teacher_id,student_id=id,new_marks=new_mark,
                                    timestamp=timezone.now())
            return redirect('home')
    return render(request,'update.html',{"form":form})

def delete(request,id):
    token = request.COOKIES.get("session_token")
    teacher_id = session_store.get(token)
    if not teacher_id:
        return redirect("login_page")
    mark=studends.objects.get(id=id)
    mark.delete()
    
    
    return redirect('home')
    
