    # -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from datetime import date
from .models import *
from .urls import *

## expenses analytics view
@login_required()
def ExpenseAnalytics(request):
    context_object_name = 'expenses'
    context ={}
    context['segment'] = "Analytics"
    context['history'] = Expense.objects.user_expenses(request.user)
    html_template = loader.get_template( 'frontend/expenses_analytics.html' )
    return HttpResponse(html_template.render(context, request))

## expenses index view
@login_required()
def ExpenseIndex(request):
    context = {}
    context['summary'] = Expense.objects.categories_summary(request.user)
    context['history'] = Expense.objects.last_ten(request.user)
    context['currencies'] = settings.CURRENCIES
    context['category_types'] = Category_type.objects.all()
    context['categories'] = Category.objects.all()
    context['cards'] = Payment.objects.all()
    context['payments'] = Expense.objects.payments_summary(request.user)
    context['form'] = ExpenseForm()
    context['segment'] = "Expenses"
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.user = request.user
            new_expense.date = date.today()
            new_expense.category_type = new_expense.category.category_type
            new_expense.save()
            return redirect( 'expenses' )
        else:
            msg = form.errors
            return render(request, 'frontend/expenses_index.html', {'context':context, 'msg':msg})
    else:
        msg = None
        return render(request, 'frontend/expenses_index.html', {'context':context, 'msg':msg})

## delete expense view
@login_required()
def DeleteExpense(request, expense_id):
    try:
        expense_edit = Expense.objects.get(user=request.user, id=expense_id)
        expense_edit.deleted = True
        expense_edit.save()
        return redirect( 'expenses' )
    except ObjectDoesNotExist:
        return redirect( 'expenses' )

## edit expense veiw
@login_required()
def EditExpense(request, expense_id):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            new_expense = form.save()
            return redirect( 'expenses' )
        else:
            msg = form.errors
            return redirect( 'edit_expenses' )
    else:
        msg = None
        try:
            expense_edit = Expense.objects.get(user=request.user, id=expense_id)
            return render(request, 'frontend/expenses_edit.html', {'expense':expense_edit, 'msg':msg})
        except ObjectDoesNotExist:
            return redirect( 'expenses' )