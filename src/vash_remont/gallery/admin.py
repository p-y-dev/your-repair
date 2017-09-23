from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Gallery, Image


class ImageInline(admin.TabularInline):
    model = Image
    ordering = "-datetime",


class GalleryAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    ordering = "-my_order",


admin.site.register(Gallery, GalleryAdmin)
