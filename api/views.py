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
    serializer = ExpenseSerializer(expenses, many="true")
    return Response(serializer.data)


# @api_view(['GET'])
def ExpensesApi(request):
    expenses = [
    {
        "id": 30,
        "date": "2022-04-04",
        "amount": 4455,
        "currency": "EGP",
        "category": 3,
        "note": "ggggg",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 29,
        "date": "2022-04-04",
        "amount": 1234,
        "currency": "EGP",
        "category": 4,
        "note": "qqqq",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 28,
        "date": "2022-04-04",
        "amount": 1234,
        "currency": "EGP",
        "category": 2,
        "note": "ddd",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 27,
        "date": "2022-03-24",
        "amount": 124,
        "currency": "EGP",
        "category": 19,
        "note": "fuel",
        "payment": 1,
        "category_type": 4,
        "deleted": "true"
    },
    {
        "id": 26,
        "date": "2022-03-22",
        "amount": 30,
        "currency": "EGP",
        "category": 4,
        "note": "2ahwa",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 25,
        "date": "2022-03-22",
        "amount": 3500,
        "currency": "EGP",
        "category": 20,
        "note": "40km service",
        "payment": 3,
        "category_type": 4,
        "deleted": "true"
    },
    {
        "id": 24,
        "date": "2022-03-22",
        "amount": 150,
        "currency": "EGP",
        "category": 19,
        "note": "Fuel regil",
        "payment": 2,
        "category_type": 4,
        "deleted": "false"
    },
    {
        "id": 23,
        "date": "2022-03-22",
        "amount": 1234,
        "currency": "EGP",
        "category": 7,
        "note": "Gardening tools",
        "payment": 1,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 22,
        "date": "2022-03-22",
        "amount": 2243,
        "currency": "EGP",
        "category": 25,
        "note": "Kick boxing subscription for 2 months",
        "payment": 2,
        "category_type": 5,
        "deleted": "false"
    },
    {
        "id": 21,
        "date": "2022-03-22",
        "amount": 724,
        "currency": "EGP",
        "category": 27,
        "note": "null",
        "payment": 3,
        "category_type": 5,
        "deleted": "true"
    },
    {
        "id": 20,
        "date": "2022-03-21",
        "amount": 990,
        "currency": "EGP",
        "category": 33,
        "note": "null",
        "payment": 2,
        "category_type": 6,
        "deleted": "true"
    },
    {
        "id": 19,
        "date": "2022-03-21",
        "amount": 43556,
        "currency": "EGP",
        "category": 32,
        "note": "null",
        "payment": 4,
        "category_type": 6,
        "deleted": "true"
    },
    {
        "id": 18,
        "date": "2022-03-21",
        "amount": 347,
        "currency": "EGP",
        "category": 5,
        "note": "null",
        "payment": 3,
        "category_type": 2,
        "deleted": "true"
    },
    {
        "id": 17,
        "date": "2022-03-21",
        "amount": 299,
        "currency": "EGP",
        "category": 1,
        "note": "null",
        "payment": 1,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 16,
        "date": "2022-03-20",
        "amount": 342,
        "currency": "EGP",
        "category": 20,
        "note": "null",
        "payment": 1,
        "category_type": 4,
        "deleted": "true"
    },
    {
        "id": 15,
        "date": "2022-03-20",
        "amount": 300,
        "currency": "EGP",
        "category": 12,
        "note": "null",
        "payment": 1,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 14,
        "date": "2022-03-20",
        "amount": 27500,
        "currency": "EGP",
        "category": 14,
        "note": "null",
        "payment": 3,
        "category_type": 3,
        "deleted": "false"
    },
    {
        "id": 13,
        "date": "2022-03-19",
        "amount": 555,
        "currency": "USD",
        "category": 4,
        "note": "1",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 12,
        "date": "2022-03-19",
        "amount": 5563,
        "currency": "EGP",
        "category": 29,
        "note": "null",
        "payment": 3,
        "category_type": 5,
        "deleted": "true"
    },
    {
        "id": 11,
        "date": "2022-03-19",
        "amount": 1234,
        "currency": "EGP",
        "category": 5,
        "note": "null",
        "payment": 1,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 10,
        "date": "2022-03-19",
        "amount": 150,
        "currency": "EGP",
        "category": 19,
        "note": "null",
        "payment": 1,
        "category_type": 4,
        "deleted": "false"
    },
    {
        "id": 9,
        "date": "2022-03-19",
        "amount": 450,
        "currency": "EGP",
        "category": 9,
        "note": "null",
        "payment": 2,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 8,
        "date": "2022-03-19",
        "amount": 3344,
        "currency": "EGP",
        "category": 8,
        "note": "null",
        "payment": 1,
        "category_type": 2,
        "deleted": "true"
    },
    {
        "id": 7,
        "date": "2022-03-18",
        "amount": 1222,
        "currency": "EGP",
        "category": 4,
        "note": "null",
        "payment": 2,
        "category_type": 1,
        "deleted": "true"
    },
    {
        "id": 6,
        "date": "2022-03-18",
        "amount": 124,
        "currency": "EGP",
        "category": 4,
        "note": "null",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 5,
        "date": "2022-03-18",
        "amount": 133,
        "currency": "EGP",
        "category": 6,
        "note": "null",
        "payment": 2,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 4,
        "date": "2022-03-18",
        "amount": 4567,
        "currency": "EGP",
        "category": 2,
        "note": "null",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 3,
        "date": "2022-03-17",
        "amount": 555,
        "currency": "EGP",
        "category": 3,
        "note": "null",
        "payment": 2,
        "category_type": 1,
        "deleted": "false"
    },
    {
        "id": 2,
        "date": "2022-03-17",
        "amount": 4455,
        "currency": "EGP",
        "category": 5,
        "note": "null",
        "payment": 2,
        "category_type": 2,
        "deleted": "false"
    },
    {
        "id": 1,
        "date": "2022-03-17",
        "amount": 1234,
        "currency": "EGP",
        "category": 3,
        "note": "null",
        "payment": 1,
        "category_type": 1,
        "deleted": "false"
    }
]
    return JsonResponse(expenses, safe=False)

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = [{
            'date': '6-4-2022'
        }]
        return Response(None, status=status.HTTP_202_ACCEPTED)
