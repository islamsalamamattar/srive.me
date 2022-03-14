from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ("store", "amount", "date", "category", )
    search_fields = ["category", "date"]

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("name", )
    search_fields = ["name",]

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Payment)
admin.site.register(Store)
admin.site.register(Expense, ExpenseAdmin)