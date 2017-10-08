from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Video


def get_video(request):
    gallery_html_data = render_to_string(
        "modal/video/video_data.html",
        {"videos": Video.objects.all()}
    )

    return JsonResponse({
        "video_html_data": gallery_html_data
    })
