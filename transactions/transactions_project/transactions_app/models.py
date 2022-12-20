from django.db import models
from datetime import date


class Transaction(models.Model):
    transaction_date = models.DateField()
    post_date = models.DateField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    transaction_type = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.amount} - {self.description}"
