
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # EMI app routes
    path('', include('emi.urls', namespace='emi')),  # Include 'emi' app URLs with namespace

    # Add a redirect for accounts/login
    re_path(r'^accounts/login/$', lambda request: redirect('emi:login')),  # Redirect to the 'login' page
]
