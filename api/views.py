from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import views

from django.contrib.auth.decorators import login_required

from expenses import models as exp
from . import serializer
from .serializer import ExpenseSerializer, LoginSerializer
from django.http import JsonResponse



@api_view(['GET'])
@login_required(login_url='api/login/')
def ExpenseIndexApi(request):
    expenses = exp.Expense.objects.filter(user=request.user).order_by('-date', '-id')
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
def ExpensesApi(request):
    expenses = exp.Expense.objects.all().order_by('-date', '-id')
    serializer = ExpenseSerializer(expenses, many=True)
    return JsonResponse(serializer.data)

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = [{
            'date': '6-4-2022'
        }]
        return Response(None, status=status.HTTP_202_ACCEPTED)
