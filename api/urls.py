from django.urls import path
from api import views

urlpatterns = [
    path("api/", views.ExpenseIndexApi, name="expenses_api"),
    path('api/login/', views.LoginView.as_view()),
]