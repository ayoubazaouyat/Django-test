from django.shortcuts import render,redirect
from projapp.forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'projapp/index.htm')

@csrf_exempt
def register(request):
    registered = False
    form= UserForm
    if request.method == 'POST':
       form= UserForm(request.POST)
       if form.is_valid() :
           form.save()
           registered = True
    return render(request,'projapp/register.htm',{'register':form,
                                                    'registered':registered
    })
def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request, username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.info(request,'Invalid Username or password')
        else:
            print("Someone triend to login ")
            print("Username:{} and password: {}".format(username,password))
            return HttpResponse("INVALID DETAILS")
    else:
        return render(request,'projapp/login.htm')

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))