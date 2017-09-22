from django.shortcuts import render
from vash_remont.gallery.models import Image


def home_page(request):

    images = Image.objects.all()

    return render(request, "index.html", {
        "main_images_gallery": images[:4],
        "all_images_gallery": images[4:],
    })
