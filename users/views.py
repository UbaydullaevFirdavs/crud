from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from users.forms import SingUpForm, SingInForm

def sign_up(request):
    if request.method =='POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    form = SingUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method =='POST':
        form = SingInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('article_func')
    form = SingInForm()
    return render(request, 'sign_in.html', {'form': form})
# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('sign_in')
