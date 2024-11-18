# emi/urls.py

from django.urls import path
from . import views

# Register app namespace
app_name = 'emi'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_emi/', views.add_emi, name='add_emi'),
    path('emi_list/', views.emi_list, name='emi_list'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_emi_payment/<int:emi_id>/', views.update_emi_payment, name='update_emi_payment'),
]
