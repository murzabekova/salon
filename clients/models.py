from django.db import models
from fillials.models import FillialServices


# Create your models here.


class Clients(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    service = models.ForeignKey(FillialServices, default=None)
    name = models.CharField(max_length=45, default=None)
    phone = models.CharField(max_length=12, default=None)
    email = models.CharField(max_length=30, default=None)
    comments = models.CharField(max_length=255, default=None)
    active = models.BooleanField(default=False)
    number = models.CharField(max_length=5, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
