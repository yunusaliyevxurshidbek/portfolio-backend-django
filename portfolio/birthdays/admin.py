from django.contrib import admin
from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    list_filter = ("date",)
    search_fields = ("name",)

