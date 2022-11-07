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

## todo index view
@login_required()
def TodoIndex(request):
    context = {}
    context['not_completed'] = Todo.objects.not_completed(request.user)
    context['all_todos'] = Todo.objects.all_todos(request.user)
    context['tod_cat'] = Category.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.date = date.today()
            new_todo.category_type = new_todo.category.category_type
            new_todo.save()
            return redirect( 'todo' )
        else:
            msg = form.errors
            return render(request, 'frontend/todo_index.html', {'context':context, 'msg':msg})
    else:
        msg = None
        return render(request, 'frontend/todo_index.html', {'context':context, 'msg':msg})
