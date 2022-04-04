from django.urls import path
from api import views

urlpatterns = [
    path("api/", views.ExpenseIndexApi, name="expenses_api"),
    path("api/test", views.ExpenseApi, name="api"),
    path('api/login/', views.LoginView.as_view()),
]