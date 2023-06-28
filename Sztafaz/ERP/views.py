from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            print(request.user)
            return render(request, 'ERP/home.html')
        else:
            query = request.POST['q']
            if query == '1':
                return render(request, 'ERP/add_purchase.html')
            else:
                return render(request, 'ERP/home.html')
    else:
        return redirect('loginuser')


def search(request):
    query = request.GET.get('q')



def loginuser(request):
    if request.method == 'GET':
        return render(request, 'ERP/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ERP/login.html', {'form': AuthenticationForm, 'error': 'Invalid password or username'})


def logoutuser(request):
    logout(request)
    return redirect('home')
