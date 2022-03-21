from calendar import month
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from datetime import *
from django.conf import settings
#from djmoney.models.fields import MoneyField
from django.forms import ModelForm
from django.utils.timezone import timedelta

# Expense Category types
class Category_type(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length= 64, null=True, blank=True)
    icon = models.CharField(max_length= 64, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = 'Category Type'

# Expense Categories
class Category(models.Model):
    name = models.CharField(max_length=25)
    category_type = models.ForeignKey(Category_type, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.CharField(max_length= 64, null=True, blank=True)
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

#Expense Object Manager
class ExpenseManger(models.Manager):
    def last_ten(self, user):
        return self.filter(user=user).order_by('-pk')[:10:1]

    def user_expenses(self, user):
        return self.filter(user=user).order_by('-pk')

    def categories_summary(self, user):
        current_month = datetime.now().month
        last_month = datetime.now().month - 1
        last_expenses = self.filter(user=user, date__month=last_month).values('category_type__name').annotate(total=Sum('amount')).order_by('-total')
        month_expenses = self.filter(user=user, date__month=current_month).values(name='category_type__name' , icon='category_type__icon' ).annotate(total=Sum('amount')).order_by('-total')
        summary = month_expenses
        return summary

    def payments_summary(self, user):
        
        current_month = datetime.now().month
        last_month = datetime.now().month - timedelta(month=1)
        month_expenses = self.filter(user=user, date__month=current_month)
        last_expenses = self.filter(user=user, date__month=last_month)
        summary = self.values('payment').annotate(total=Sum('amount'))
        return summary

    def get_context(self, user):
        context={}
        context['history'] = self.last_ten(user)
        context['summary'] = self.categories_summary(user)
        return context


# Expense object
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True, )
    amount = models.PositiveIntegerField()
    currency = models.CharField('Currency', max_length=3, choices = [('EGP', 'EGP'), ('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED')])
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_type = models.ForeignKey(Category_type, null=True, blank=True, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE)
    objects = ExpenseManger()
    def __str__(self):
        return f"{self.category} , {self.amount}"


class ExpenseForm(ModelForm):
    '''
    def __init__(self, current_user, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = self.fields['category'].queryset.filter(user__in = [current_user, 1])
        self.fields['store'].queryset = self.fields['store'].queryset.filter(user=current_user)
        self.fields['payment'].queryset = self.fields['payment'].queryset.filter(user=current_user)
    '''
    class Meta:
        model = Expense
        fields = ('amount', 'currency', 'category', 'store', 'deleted', 'payment')

