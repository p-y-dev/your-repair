from django.urls import path

from .views import create_reviews

app_name = 'reviews'


urlpatterns = [
    path('create', create_reviews, name="create_reviews"),
]
