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
    html_template = loader.get_template( 'frontend/todo_index.html' )
    return HttpResponse(html_template.render(context, request))