"""
URL configuration for emi_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# emi_tracker/urls.py
from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import redirect
from emi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('emi/signup/', views.signup_view, name='signup'),
    path('emi/login/', views.login_view, name='login'),
    path('emi/logout/', views.logout_view, name='logout'),
    path('emi/add_emi/', views.add_emi, name='add_emi'),
    path('emi/emi_list/', views.emi_list, name='emi_list'),
    path('emi/add_transaction/', views.add_transaction, name='add_transaction'),
    path('emi/transaction_list/', views.transaction_list, name='transaction_list'),
    # Add a redirect for accounts/login
    re_path(r'^accounts/login/$', lambda request: redirect('login')),
]
