from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Gallery


def get_galleries(request):
    gallery_html_data = render_to_string(
        "modal/gallery/gallery_data.html",
        {"galleries": Gallery.objects.all()}
    )

    return JsonResponse({
        "gallery_html_data": gallery_html_data
    })
