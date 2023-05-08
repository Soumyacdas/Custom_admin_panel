from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def adminlogin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(adminpage)
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect(adminpage)
            else:
                return render(request,'adminlogin.html')
        else:
            return render(request,'adminlogin.html')

    return render(request,'adminlogin.html')
@never_cache
def adminpage(request):
    if request.user.is_authenticated:
        users=User.objects.all()
        details={'users':users}
        return render(request,'adminpage.html',details)
    else:
        return redirect(adminlogin)
def search(request):
    if request.method == 'GET':
        query=request.GET.get('query')
        if query:
            user=User.objects.filter(username__icontains=query)
            details={'user':user}
            return render(request,'adminsearch.html',details)
    return redirect(adminpage)
def adminlogout(request):
    logout(request)
    return redirect('adminlogin')
def admindelete(request,id):
    User.objects.get(id=id).delete()
    return redirect(adminpage)
def userupdate(request,id):
    user=User.objects.get(id=id)
    details={'user':user}
    return render(request,'userupdate.html',details)
def doupdate(request,id):
    u_firstname=request.POST.get('first_name')
    u_lastname=request.POST.get('last_name')
    u_username=request.POST.get('username')
    u_email=request.POST.get('email')

    user=User.objects.get(pk=id)
    user.first_name=u_firstname
    user.last_name=u_lastname
    user.username=u_username
    user.email=u_email
    user.save()
    return redirect(adminpage)
def adduser(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            return HttpResponse("Passwords are not same!!!")
        if User.objects.filter(username=username).exists():
            return HttpResponse("username already taken")
        else:
            new_user=User.objects.create_user(username,email,password)
            new_user.first_name=first_name
            new_user.last_name=last_name
            new_user.save()
            return redirect(adminpage)
    return render(request,'adduser.html')