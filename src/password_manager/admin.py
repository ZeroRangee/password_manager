from django.contrib import admin
from password_manager.models import EntryPassword


@admin.register(EntryPassword)
class AdminEntryPassword(admin.ModelAdmin):
    pass
