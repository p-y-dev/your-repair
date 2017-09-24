from django.conf.urls import url
from .views import get_galleries

urlpatterns = [
    url(r'^$', get_galleries, name="get_galleries"),
]