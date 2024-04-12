# Import necessary modules
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# View function for user signup
def signup(request):
    # Create form instance
    form = CreateUserForm()
    
    # Check if form is submitted
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        # Validate form data
        if form.is_valid():
            # Save user data
            form.save()
            # Redirect to signin page
            return redirect('signin')
   
    # Prepare context data
    context = {'signupform': form}

    # Render signup page with form
    return render(request, 'signup.html', context=context)

# View function for user signin
def signin(request):
    # Create form instance
    form = LoginForm()

    # Check if form is submitted
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # Validate form data
        if form.is_valid():
            # Get username and password from form data
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            # If user is authenticated, log them in and redirect to dashboard
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            
    # Prepare context data
    context = {'loginform': form}

    # Render signin page with form
    return render(request, 'login.html', context=context)

# View function for home page
def home(request):
    # Render home page
    return render(request, 'home.html')

# View function for about page
def about(request):
    # Render about page
    return render(request, 'about.html')

# View function for contact page
def contact(request):
    # Render contact page
    return render(request, 'contact.html')

# View function for dashboard page
def dashboard(request):
    # Render dashboard page
    return render(request, 'dashboard.html')

# View function for user signout
def signout(request):
    # Log user out and redirect to home page
    logout(request)
    return redirect('home')
