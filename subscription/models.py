from django.db import models

from expenses.models import *


# Create your models here.
class Subsription(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category_type, on_delete=models.CASCADE)
    type = models.CharField('subcription/installment', max_length=12, choices = [('S', 'Subsription'), ('I', 'Installment')])
    frequency = models.CharField('Due', max_length=12, choices = [('1', 'Monthly'), ('3', 'Quarterly'), ('12', 'Yearly')])
    next_due = models.DateField()
    autopay = models.BooleanField(default=True)

