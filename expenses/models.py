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
from dateutil.relativedelta import relativedelta

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


# Expense Object Manager
class ExpenseManger(models.Manager):
    ## return a list of last ten expenses from all categories
    def last_ten(self, user):
        return self.filter(user=user, deleted=False).order_by('-pk')[:10:1]
    ## full list of user expenses
    def user_expenses(self, user):
        return self.filter(user=user, deleted=False).order_by('-pk')
    ## summary of CURRENT month expenses by categpry_type
    def categories_summary(self, user):
        current_month = datetime.now().month
        month_expenses = self.filter(user=user, date__month=current_month, deleted=False).values('category_type__name' , 'category_type__icon', 'category_type__color').annotate(total=Sum('amount')).order_by('-total')
        summary = month_expenses
        return summary
    ## summary of LAST month expenses by categpry_type
    def categories_summary_last(self, user):
        last_month = datetime.now().month - 1
        last_expenses = self.filter(user=user, date__month=last_month, deleted=False).values('category_type__name' , 'category_type__icon', 'category_type__color').annotate(total=Sum('amount')).order_by('-total')
        summary = last_expenses
        return summary
    ## summary of CURRENT month expenses by payment method
    def payments_summary(self, user):       
        current_month = datetime.now().month
        summary = self.filter(user=user, date__month=current_month, deleted=False).values('payment__name').annotate(total=Sum('amount')).order_by('-total')
        return summary
    ## summary of Last month expenses by payment method
    def payments_summary_last(self, user):
        last_month = datetime.now().month - 1
        summary = self.filter(user=user, date__month=last_month, deleted=False).values('payment__name').annotate(total=Sum('amount')).order_by('-total')
        return summary


# Expense object
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True, )
    amount = models.PositiveIntegerField()
    currency = models.CharField('Currency', max_length=3, choices = [('EGP', 'EGP'), ('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED')])
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_type = models.ForeignKey(Category_type, null=True, blank=True, on_delete=models.CASCADE)
    note = models.CharField(max_length=140, null=True, blank=True)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField('Type', max_length=12, choices = [('S', 'Subsription'), ('I', 'Installment'), ('E', "Expense")], default='E')
    objects = ExpenseManger()
    def __str__(self):
        return f"{self.category} , {self.amount}"

# ExpenseForm
class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'currency', 'category', 'note', 'deleted', 'payment')


# Subscriptions Mabager
class SubscriptionManager(models.Manager):
    ## returns due subscriptions that are set to manual pay
    def to_be_paid_manual(self, user):
        subscriptions = self.filter(user=user, autopay=False, date__lte=datetime.date.today())
        return subscriptions
    ## auto paying >> creating expense for due subscription set to autopay
    def auto_pay(self, user):
        subscriptions = self.filter(user=user, autopay=True, date__lte=datetime.today())
        for subscription in subscriptions:
            payment = Expense(
                user=user,
                amount=subscription.amount,
                currency=subscription.currency,
                category=subscription.category,
                category_type=subscription.category.category_type,
                note=subscription.note+subscription.frequency+' subscription',
                payment=subscription.payment,
                type=subscription.type,
                )
            newexpense = payment.save()
            newexpense.date=subscription.next_due
            newexpense.save()
            subscription.next_due += relativedelta(months=int(subscription.frequency))
            subscription.save()

# Subscription and installments            
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True, )
    amount = models.PositiveIntegerField()
    currency = models.CharField('Currency', max_length=3, choices = [('EGP', 'EGP'), ('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED')])
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_type = models.ForeignKey(Category_type, null=True, blank=True, on_delete=models.CASCADE)
    note = models.CharField(max_length=140, null=True, blank=True)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField('Type', max_length=12, choices = [('S', 'Subsription'), ('I', 'Installment')], default='S')

    frequency = models.CharField('Due', max_length=12, choices = [('1', 'Monthly'), ('3', 'Quarterly'), ('12', 'Yearly')])
    next_due = models.DateField()
    autopay = models.BooleanField(default=True)

    objects = SubscriptionManager()
    def __str__(self):
        return f"{self.note} , {self.amount}"

