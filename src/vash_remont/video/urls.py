from django.conf.urls import url
from .views import get_video

urlpatterns = [
    url(r'^$', get_video, name="get_video"),
]