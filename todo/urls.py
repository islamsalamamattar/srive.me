from django.urls import path
from expenses import views
from django.shortcuts import redirect


urlpatterns = [
    path('todo/', views.TodoIndex, name="todo"),
]