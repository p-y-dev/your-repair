from django.urls import path
from .views import get_galleries

app_name = 'gallery'

urlpatterns = [
    path('', get_galleries, name="get_galleries"),
]