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
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.user = request.user
            new_expense.date = date.today()
            new_expense.save()
            return redirect( 'expenses' )
        else:
            msg = form.error_class
            return render(request, 'frontend/expenses_index.html', { 'segment': "Expenses", 'msg':msg})

    else:
        context = Expense.objects.get_context(request.user)
        context['currencies'] = settings.CURRENCIES
        context['categories'] = Category.objects.filter(user = request.user) | Category.objects.filter(user = 1)
        context['stores'] = Store.objects.filter(user = request.user) | Store.objects.filter(user = 1)
        context['cards'] = Payment.objects.filter(user = request.user)
        context['summary'] = {}
        for category in context['categories']:
            total = 0
            for code in context['summary_list']:
                if code['category'] == category.id:
                    total = code['total']
                    break
            context['summary'][category] =  total
        context['summary'] = {k: v for k, v in sorted(context['summary'].items(), key=lambda item: item[1], reverse=True)}
        form = ExpenseForm()
        msg = None
        return render(request, 'frontend/expenses_index.html', {'context':context, 'form':form, 'segment': "Expenses", 'msg':msg})
