# emi/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import EMI, Transaction
from django.utils import timezone


# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'emi/dashboard.html')

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'emi/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'emi/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'emi/dashboard.html')

# View to add a new EMI entry
@login_required
def add_emi(request):
    if request.method == "POST":
        total_amount = request.POST.get('total_amount')
        monthly_payment = request.POST.get('monthly_payment')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        emi = EMI(
            user=request.user,
            total_amount=total_amount,
            monthly_payment=monthly_payment,
            paid_amount=0,
            pending_amount=total_amount,
            start_date=start_date,
            end_date=end_date,
        )
        emi.save()
        return redirect('emi_list')
    return render(request, 'emi/add_emi.html')

# View to display all EMIs for the logged-in user
@login_required
def emi_list(request):
    emis = EMI.objects.filter(user=request.user)
    return render(request, 'emi/emi_list.html', {'emis': emis})

# View to update an EMI payment
@login_required
def update_emi_payment(request, emi_id):
    emi = EMI.objects.get(id=emi_id, user=request.user)
    if request.method == "POST":
        payment = float(request.POST.get('payment'))
        emi.paid_amount += payment
        emi.pending_amount = emi.total_amount - emi.paid_amount
        emi.save()
        return redirect('emi_list')
    return render(request, 'emi/update_emi_payment.html', {'emi': emi})

# View to add a new transaction entry
@login_required
def add_transaction(request):
    if request.method == "POST":
        amount_given = request.POST.get('amount_given')
        amount_returned = request.POST.get('amount_returned')
        description = request.POST.get('description')

        transaction = Transaction(
            user=request.user,
            amount_given=amount_given,
            amount_returned=amount_returned,
            description=description,
            transaction_date=timezone.now()
        )
        transaction.save()
        return redirect('transaction_list')
    return render(request, 'emi/add_transaction.html')

# View to display all transactions for the logged-in user
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'emi/transaction_list.html', {'transactions': transactions})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'emi/login.html', {'form': form})
