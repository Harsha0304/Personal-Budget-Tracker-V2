from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import EMI, Transaction
from django.utils import timezone

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('emi:dashboard')  # Updated namespace
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
            return redirect('emi:dashboard')  # Updated namespace
    else:
        form = AuthenticationForm()
    return render(request, 'emi/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('emi:login')  # Updated namespace

# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'emi/dashboard.html')

# View to add a new EMI entry
@login_required
def add_emi(request):
    if request.method == "POST":
        total_amount = float(request.POST.get('total_amount', 0))
        monthly_payment = float(request.POST.get('monthly_payment', 0))
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
        return redirect('emi:emi_list')  # Updated namespace
    return render(request, 'emi/add_emi.html')

# View to display all EMIs for the logged-in user
@login_required
def emi_list(request):
    emis = EMI.objects.filter(user=request.user)
    return render(request, 'emi/emi_list.html', {'emis': emis})

# View to update an EMI payment
@login_required
def update_emi_payment(request, emi_id):
    emi = get_object_or_404(EMI, id=emi_id, user=request.user)
    if request.method == "POST":
        payment = float(request.POST.get('payment', 0))
        emi.paid_amount += payment
        emi.pending_amount = emi.total_amount - emi.paid_amount
        emi.save()
        return redirect('emi:emi_list')  # Updated namespace
    return render(request, 'emi/update_emi_payment.html', {'emi': emi})

# View to add a new transaction entry
@login_required
def add_transaction(request):
    if request.method == "POST":
        amount_given = float(request.POST.get('amount_given', 0))
        amount_returned = float(request.POST.get('amount_returned', 0))
        description = request.POST.get('description')

        transaction = Transaction(
            user=request.user,
            amount_given=amount_given,
            amount_returned=amount_returned,
            description=description,
            transaction_date=timezone.now(),
        )
        transaction.save()
        return redirect('emi:transaction_list')  # Updated namespace
    return render(request, 'emi/add_transaction.html')

# View to display all transactions for the logged-in user
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'emi/transaction_list.html', {'transactions': transactions})
def add_transaction(request):
    # Handle the form submission or the process of adding a transaction here
    return render(request, 'emi/add_transaction.html')