from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class ItemAdmin(ImportExportModelAdmin):
    list_display = ("category", "item", "date_added")
    search_fields = ["category", "item", "date_added"]


# Register your models here.
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)