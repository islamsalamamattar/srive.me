from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ("id", "category_type", "amount", "date", "category", "note")
    search_fields = ["category", "date", "note"]

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("name", "category_type")
    search_fields = ["category_type", "name"]

# Register your models here.
admin.site.register(Category_type)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Payment)
admin.site.register(Store)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Subscription)
admin.site.register(Budget)
