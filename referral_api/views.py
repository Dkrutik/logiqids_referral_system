from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json
import uuid

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        name = data.get('name')
        city = data.get('city')
        referral_code = data.get('referral_code')
        password = data.get('password')

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        # Generate a unique referral code
        generated_code = str(uuid.uuid4())[:8]

        user = CustomUser.objects.create_user(email=email, name=name, city=city, referral_code=referral_code, password=password, generated_code=generated_code)
        return JsonResponse({'message': 'Registration successful', 'generated_code': generated_code})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'message': 'Login successful',
                'redirect_url': '/home/',
                'user': {
                    'email': user.email,
                    'name': user.name,
                    'city': user.city,
                    'referral_code': user.referral_code,
                    'generated_code': user.generated_code
                }
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'})
