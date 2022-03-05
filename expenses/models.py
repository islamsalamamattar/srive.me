from django.contrib.auth.models import User
from django.db import models
from datetime import *
from djmoney.models.fields import MoneyField

# Expense Categories
class Category(models.Model):
    name = models.CharField(max_length=25)
    logo = models.ImageField(blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = 'Categories'

# Payment Methods
class Payment(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField('Account type', max_length=25, choices = [('DB', 'Debit Account'), ('CC', 'Credit Card'), ('WK', 'Work Card')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'

# Stores
class Store(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

# Expense object
class Expense(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=7, decimal_places=2, default_currency='EGP')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.category} , {self.value}"