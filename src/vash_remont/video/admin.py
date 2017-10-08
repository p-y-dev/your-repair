from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Video


class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):

    ordering = "-my_order",


admin.site.register(Video, VideoAdmin)
