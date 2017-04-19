from django.db import models

# Create your models here.


class Services(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    title = models.CharField(max_length=45)

    def __str__(self):
        return self.title
