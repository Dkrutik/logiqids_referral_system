from django.urls import path
from .views import register_view, login_view, logout_view, home_view ,referral_ajax_page

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('referrals/', referral_ajax_page, name='referral-ajax-page'),
   
]
