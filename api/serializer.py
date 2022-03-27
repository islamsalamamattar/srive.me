from rest_framework import serializers
from expenses import models

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = ['id', 'date', 'amount', 'currency', 'category', 'note', 'payment', 'category_type', 'deleted']

