from rest_framework.decorators import api_view
from rest_framework.response import Response
from expenses import models
from .serializer import ExpenseSerializer


@api_view(['GET'])
def ExpenseIndexApi(request):
    expenses = models.Expense.objects.all().order_by('-date', '-id')
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)
