from django.db import models
from django.contrib.auth.models import User
from services.models import Services

# Create your models here.


class Fillials(models.Model):
    """ Fillial or Salon """
    class Meta:
        verbose_name = 'Филлиал'
        verbose_name_plural = 'Филлиалы'
    user = models.OneToOneField(User)
    title = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='fillals/avatars', null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Картинка для галереи'
        verbose_name_plural = 'Картинки для галереи'
    title = models.CharField(max_length=45)
    fillial = models.ForeignKey(Fillials)
    image = models.ImageField(upload_to='fillials/gallery')
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.title


class FillialServices(models.Model):
    class Meta:
        verbose_name = 'Услуга филлиала'
        verbose_name_plural = 'Услуги филлиала'
    service_title = models.ForeignKey(Services, default=None)
    price = models.IntegerField()
    fillal = models.ForeignKey(Fillials)

    def __str__(self):
        return self.service_title
