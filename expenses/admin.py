from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ("store", "amount", "date", "category", )
    search_fields = ["category", "date"]


# Register your models here.
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Store)
admin.site.register(Expense, ExpenseAdmin)