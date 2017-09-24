from django.http import JsonResponse
from django.shortcuts import render

from vash_remont.gallery.models import Gallery, Image
from vash_remont.reviews.models import Review, APPROVED

from vash_remont.settings_site.models import SettingsSite


def home_page(request):

    images = Image.objects.order_by('?').all()[:4]
    galleries = Gallery.objects.all()

    reviews = Review.objects.filter(state=APPROVED).all()
    main_reviews = reviews.order_by('?')[:3]

    settings_site = SettingsSite.objects.first()

    if settings_site is None:
        settings_site = {
            "email": "",
            "number_phone": "",
            "youtube_link": "#",
            "vk_link": "#",
            "twitter_link": "#",
            "google_plus_link": "#"
        }

    return render(request, "index.html", {
        "main_images": images,
        "galleries": galleries,

        "main_reviews": main_reviews,
        "reviews": reviews,

        "settings_site": settings_site
    })


def send_application(request):
    initials = request.GET['initials']
    phone = request.GET['phone']

    return JsonResponse({
        "initials": initials,
        "phone": phone,
    })
