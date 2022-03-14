# -*- encoding: utf-8 -*-

from django.urls import path
from expenses import views
from django.shortcuts import redirect


urlpatterns = [
    #path('', lambda req: redirect('expenses')),
    path('expenses/', views.ExpenseIndex, name="expenses"),
    path('expenses/analytics', views.ExpenseAnalytics, name='analytics'),
]
