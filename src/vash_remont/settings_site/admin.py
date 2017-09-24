from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from .models import SettingsSite


class SettingsSiteAdmin(SingleModelAdmin):
    pass


admin.site.register(SettingsSite, SettingsSiteAdmin)
