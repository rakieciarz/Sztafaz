from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Vendors, OrderHeader, OrderDetails


# Create your views here.


def home(request):
    # check if user is logged
    if request.user.is_authenticated:
        # return home page if method is GET
        if request.method == 'GET':
            print(request.user)
            return render(request, 'ERP/home.html')
        # if method is POST
        else:
            # Check if requested function exists
            query = search(request.POST['q'])
            # If so, return the given function
            if query is not None:
                return render(request, query[0], query[1])
            else:
                return render(request, 'ERP/home.html', {'error': 'No function you called'})
    else:
        return redirect('loginuser')


def search(query):
    # Add another function No. and path to HTML file
    mapping = {'1': 'ERP/add_purchase.html',
               }
    # Check if function exists
    try:
        # Vendor data
        vendors = Vendors.objects.all()
        results = [mapping[query], {'vendors': vendors}]
        return results
    except KeyError:
        return None


def loginuser(request):
    # return authentication form to logging if method GET
    if request.method == 'GET':
        return render(request, 'ERP/login.html', {'form': AuthenticationForm})
    # check if given username and password is correct
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # if so, login and return home page
        if user is not None:
            login(request, user)
            return redirect('home')
        # raise error that username or password didnt match
        else:
            return render(request, 'ERP/login.html', {'form': AuthenticationForm, 'error': 'Invalid password or username'})


def logoutuser(request):
    logout(request)
    return redirect('home')


# My functions
def purchasing_order(request):
    if request.method == "POST":
        pass
    else:
        return redirect('home')