from django.http import JsonResponse
from django.shortcuts import render
from .models import Review


def create_reviews(request):
    initials = request.GET['initials']
    review = request.GET['review']

    Review.objects.create(
        name_user=initials,
        review_text=review
    )

    return JsonResponse({
        "initials": initials,
        "review": review,
    })
