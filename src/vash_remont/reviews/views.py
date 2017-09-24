from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Review
from django.conf import settings


def create_reviews(request):
    initials = request.GET['initials']
    review = request.GET['review']

    Review.objects.create(
        name_user=initials,
        review_text=review
    )

    status_send = send_mail(
        'Отзыв на сайт', 'Инициалы: ' + initials + "\n\nОтзыв: " + review,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]
    )

    if status_send == 1:
        return JsonResponse({
            "success": True,
        })
    else:
        return JsonResponse({
            "success": False,
        })

