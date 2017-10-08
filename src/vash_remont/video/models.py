from django.db import models


class Video(models.Model):
    class Meta:
        verbose_name_plural = "Видео"
        verbose_name = "Видео"
        ordering = "-my_order",

    name = models.CharField(
        verbose_name="Название видео",
        max_length=254,
    )

    iframe = models.TextField(
        verbose_name="iframe видео",
        help_text="Чтобы вставить iframe, нужно на youtube под видео нажать на 'поделиться', затем нажать на встроить,"
                  " и скопировать тег iframe.",
        max_length=9000,
    )

    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
