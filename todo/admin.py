from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class TodoAdmin(ImportExportModelAdmin):
    list_display = ("category", "task", "date_added")
    search_fields = ["category", "task", "date_added"]


# Register your models here.
admin.site.register(Category)
admin.site.register(Todo, TodoAdmin)