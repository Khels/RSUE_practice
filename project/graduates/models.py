from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Graduate(models.Model):
    first_name = models.CharField(
        _('Имя'),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        _('Фамилия'),
        max_length=150,
        blank=True,
    )
    patronym = models.CharField(
        _('Отчество'),
        max_length=150,
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to='graduates/',
        blank=True,
        verbose_name='Фотография',
    )
    graduated = models.IntegerField(
        _('Год выпуска'),
        default=2021,
        validators=[MinValueValidator(1950),
                    MaxValueValidator(2021)],
    )
    faculty = models.CharField(
        _('Факультет'),
        max_length=200,
        blank=True,
        null=True,
    )
    cafedra = models.CharField(
        _('Кафедра'),
        max_length=500,
        blank=True,
        null=True,
    )
    career = models.TextField(
        _('Карьера'),
    )
    contacts = models.TextField(
        _('Контакты'),
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.patronym:
            return f'{self.last_name} {self.first_name[:1]}.{self.patronym[:1]}.'
        return f'{self.last_name} {self.first_name[:1]}.'

    def get_fullname(self):
        return str(self)

    def get_career(self):
        if len(self.career) > 70:
            return self.career[:70] + '...'
        return self.career
