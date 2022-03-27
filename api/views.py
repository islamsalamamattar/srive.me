from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from expenses import models as exp
from .serializer import ExpenseSerializer




@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def ExpenseIndexApi(request):
    expenses = exp.Expense.objects.all().order_by('-date', '-id')
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)
