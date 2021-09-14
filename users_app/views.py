from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method=='POST':
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            profile=register_form.save(commit=False)
            profile.user=request.user
            profile.save()
            messages.success(request,('New User Account Created'))
            return redirect('login')
    else:
        register_form=CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

def login(request):
    if request.method=='POST':
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            return redirect('menu')
    else:
        form=CustomRegisterForm()
    return render(request, 'login.html', {'register_form': form})