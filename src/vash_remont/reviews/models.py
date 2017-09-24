from django.db import models
from datetime import datetime

APPROVED = '1'
NOT_APPROVED = '0'

STATE_REVIEW_CHOICES = (
    (NOT_APPROVED, 'Не одобрен'),
    (APPROVED, 'Одобрен'),
)


class Review(models.Model):
    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"
        ordering = "-datetime",

    name_user = models.CharField(
        verbose_name="Имя пользователя",
        max_length=256,
    )

    review_text = models.TextField(
        verbose_name="Текст отзыва",
        max_length=2048,
    )

    state = models.CharField(
        max_length=2,
        choices=STATE_REVIEW_CHOICES,
        default=NOT_APPROVED,
    )

    datetime = models.DateTimeField(
        verbose_name="Дата и время отзыва",
        default=datetime.now,
    )

    def __str__(self):
        return self.name_user + " (" + str(self.datetime) + ")"
