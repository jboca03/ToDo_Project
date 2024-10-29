from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# Home view
def home(request):
    return render(request, "home.html")

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my_to_do_lists')  # Redirect to "My To-Do Lists" after login
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_user(request):
    logout(request)
    return redirect('home')

# "My To-Do Lists" view
def my_to_do_lists(request):
    # Only allow logged-in users to access this page
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'my_to_do_lists.html')
# about page
def about(request):
    return render(request, 'about.html')
# contact page
def contact(request):
    return render(request, 'contact.html')