from django.db import models
from django.contrib.auth.models import User  # To link EMI to a user

class EMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"EMI for {self.user.username} - {self.total_amount}"
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_given = models.DecimalField(max_digits=10, decimal_places=2)
    amount_returned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    transaction_date = models.DateField()

    def __str__(self):
        return f"Transaction for {self.user.username} - {self.amount_given}"
