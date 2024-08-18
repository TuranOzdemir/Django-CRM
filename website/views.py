from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

 

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # If user is found
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.error(request, ('Error logging in - Please try again'))
            return redirect('home')
        
    else:
        return render(request, 'home.html', {'records': records})
        




def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Successfully registered!'))
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, ('Record has been added'))
                return redirect('home')
        
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, ('Please log in to add a record'))
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        if request.method == 'POST':
            form = AddRecordForm(request.POST or None, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, ('Record has been updated'))
                return redirect('home')
        else:
            form = AddRecordForm(instance=current_record)
        return render(request, 'update_record.html', {'form': form, 'customer_record': current_record})
    else:
        messages.error(request, ('Please log in to update this record'))
        return redirect('home')
        

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, ('Please log in to view this record'))
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, ('Record has been deleted'))
        return redirect('home')
    else:
        messages.error(request, ('Please log in to delete this record'))
        return redirect('home')

