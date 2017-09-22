from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Gallery, Image


class ImageInline(admin.TabularInline):
    model = Image


class GalleryAdmin(SingleModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Gallery, GalleryAdmin)
