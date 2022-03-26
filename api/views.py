from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..expenses.models import Expense
from serializer import ExpenseSerializer


@api_view('GET')
def ExpenseIndexApi(request):
    expenses = Expense.objects.all()
    serliazer = ExpenseSerializer(expenses, many=True)
    return Response(serliazer.data)
