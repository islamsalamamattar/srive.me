from rest_framework import serializers
from ..expenses.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'currency', 'category', 'note', 'payment', 'category_type', 'deleted']

