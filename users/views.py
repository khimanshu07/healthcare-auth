from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def index(request):
    if request.user.is_authenticated:
        return redirect('login_redirect')
    return render(request, 'users/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_redirect')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def login_redirect(request):
    if request.user.user_type == 'patient':
        return redirect('patient_dashboard')
    else:
        return redirect('doctor_dashboard')

@login_required
def patient_dashboard(request):
    return render(request, 'users/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'users/doctor_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('index')
