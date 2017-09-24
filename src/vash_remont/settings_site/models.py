from django.db import models


class SettingsSite(models.Model):
    class Meta:
        verbose_name_plural = "Настройки сайта"
        verbose_name = "Настройки сайта"

    email = models.EmailField(
        verbose_name="Электронная почта"
    )

    number_phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=20
    )

    youtube_link = models.CharField(
        verbose_name="Ссылка на youtube",
        max_length=9000
    )

    vk_link = models.CharField(
        verbose_name="Ссылка на VK",
        max_length=9000
    )

    twitter_link = models.CharField(
        verbose_name="Ссылка на twitter",
        max_length=9000
    )

    google_plus_link = models.CharField(
        verbose_name="Ссылка на google plus",
        max_length=9000
    )
