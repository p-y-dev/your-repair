from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from vash_remont.gallery.models import Gallery, Image


def home_page(request):

    images = Image.objects.order_by('?').all()[:4]
    galleries = Gallery.objects.all()

    return render(request, "index.html", {
        "main_images": images,
        "galleries": galleries
    })


def get_galleries(request):

    gallery_html_data = render_to_string(
        "modal/gallery_data.html",
        {"galleries": Gallery.objects.all()}
    )

    return JsonResponse({
        "gallery_html_data": gallery_html_data
    })
