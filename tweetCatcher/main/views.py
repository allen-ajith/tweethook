from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import TweetForm,SignUpForm
# Create your views here.

def index(request):
    return render(request, 'base.html',{})

def test(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/THANKS/')

    else:
        form = TweetForm()

    return render(request,'test.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request,'signup.html', {'form':form})