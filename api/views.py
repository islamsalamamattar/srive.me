from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..expenses.models import Expense


@api_view('GET')
def ExpenseIndexApi(request):
    expenses = Expense.objects.all()
    return Response(expenses)
