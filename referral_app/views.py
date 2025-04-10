from django.shortcuts import render

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def home_view(request):
    return render(request, 'home.html')

def referral_ajax_page(request):
    return render(request, 'referrals_ajax.html')
