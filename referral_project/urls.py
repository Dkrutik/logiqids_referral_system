from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('referral_api.urls')),
    path('', include('referral_app.urls')),
]
