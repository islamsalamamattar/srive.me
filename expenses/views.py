    # -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from datetime import date
from .models import *
from .urls import *

@login_required()
def ExpenseAnalytics(request):
    context_object_name = 'expenses'
    context ={}
    context['segment'] = "Analytics"
    html_template = loader.get_template( 'frontend/expenses_analytics.html' )
    return HttpResponse(html_template.render(context, request))

@login_required()
def ExpenseIndex(request):
    context = Expense.objects.get_context(request.user)
    context['currencies'] = settings.CURRENCIES
    context['category_types'] = Category_type.objects.all()
    context['categories'] = Category.objects.all()
    context['stores'] = Store.objects.all()
    context['cards'] = Payment.objects.all()
    context['summary'] = {k: v for k, v in sorted(context['summary'].items(), key=lambda item: item[1], reverse=True)}
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.user = request.user
            new_expense.date = date.today()
            new_expense.save()
            return redirect( 'expenses' )
        else:
            msg = form.errors
            return render(request, 'frontend/expenses_index.html', {'context':context, 'form':form, 'segment': "Expenses", 'msg':msg})

    else:
        msg = None
        return render(request, 'frontend/expenses_index.html', {'context':context, 'form':form, 'segment': "Expenses", 'msg':msg})
