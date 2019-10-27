from django.urls import path

from .views import get_video

app_name = 'video'


urlpatterns = [
    path('', get_video, name="get_video"),
]
