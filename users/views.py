from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username},you are registered ')
            return redirect('login')
        
    form=RegisterForm()
    return render(request,'users/register.html',{'form':form})
def log_out(request):
    logout(request)
    return render(request,'users/logout.html')

@login_required
def profile(request):
    return render(request,'users/profile.html')




