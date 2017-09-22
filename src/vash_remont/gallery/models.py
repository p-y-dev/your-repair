from django.db import models


class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "Галерея"


class Image(models.Model):
    class Meta:
        ordering = "-datetime",

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    image = models.ImageField(
        verbose_name="Фотография",
        upload_to = 'gallery/',
    )

    datetime = models.DateTimeField(auto_now_add=True, blank=True)
