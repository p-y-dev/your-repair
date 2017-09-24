from django.conf.urls import url
from .views import create_reviews

urlpatterns = [
    url(r'^create$', create_reviews, name="create_reviews"),
]