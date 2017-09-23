from django.db import models


class BaseImage(models.Model):
    class Meta:
        abstract = True
        ordering = "-datetime",

    image = models.ImageField(
        verbose_name="Фотография",
        upload_to='gallery/',
    )

    datetime = models.DateTimeField(auto_now_add=True, blank=True)


class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "Галерея"
        ordering = "-my_order",

    name = models.CharField(
        verbose_name="Название Галереи",
        max_length=254,
        default="",
    )

    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Image(BaseImage):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
