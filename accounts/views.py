from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth
from vendor.forms import VendorForm
from vendor.models import Vendor
from .utils import detectUser
from django.contrib.auth.decorators import login_required

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, "your already log in")
        return redirect('custDashboard')
    elif request.method == 'POST':
        
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password'] 
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            # return redirect('registerUser')


            # Create the user using create_user method
            # Extract cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Properly split the email
            email_name, domain_part = email.strip().rsplit("@", 1)

            # Create the user with cleaned data
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your account has been registered successfully")
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)


def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, "your already log in")
        return redirect('custDashboard')
    elif request.method == 'POST':
        # srore data and create a new User
        v_form = VendorForm(request.POST, request.FILES)
        form = UserForm(request.POST)
        if form.is_valid() and v_form.is_valid():
            # Create the user using the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Properly split the email
            email_name, domain_part = email.strip().rsplit("@", 1)

            # Create the user with cleaned data
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()

            # Create a new vendor
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, "Your account has been registered successfully, please wait for approval!")
            return redirect('registerVendor')
            
        else:
            print(form.errors)
            print(v_form.errors)
    else:
        form = UserForm()
        v_form = VendorForm()
    context = {
        'form': form,
        'v_form': v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "Your already log in")
        return redirect('custDashboard')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('custDashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, "You are now logged out.")
    return redirect('login')

@login_required(login_url='login') #redirect when user is not logged in
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
def custDashboard(request):
    return render(request, 'accounts/custDashboard.html')

@login_required(login_url='login')
def vendorDashboard(request):
    return render(request, 'accounts/vendorDashboard.html')
