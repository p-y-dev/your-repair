from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = "name_user", "datetime", "state",
    list_filter = "state", "datetime"
    ordering = "-datetime",


admin.site.register(Review, ReviewAdmin)
