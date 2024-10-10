from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Signed UP!!')
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form,'type':'register'})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'Successfully Logedout')
    return redirect('homepage')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pasword = form.cleaned_data['password']
            user = authenticate(username=name,password=pasword)
            if user is not None:
                login(request,user)
                messages.success(request,'Logedin Successfully!!')
                return redirect('profilepage')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form,'type':'Login'})

@login_required
def change_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profilepage')
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'register.html',{'form':form,'type':'Change password'})
    
@login_required
def set_user_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profilepage')
        
    else:
        form = SetPasswordForm(request.user)
    return render(request,'register.html',{'form':form,'type':'Set password'})
    
