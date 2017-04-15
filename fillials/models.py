from django.db import models
from django.contrib.auth.models import User
# from fillials.mics import get_upload_path

# Create your models here.


class Fillials(models.Model):
    """ Fillial or Salon """
    user = models.OneToOneField(User)
    title = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='fillals/avatars', null=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=45)
    fillial = models.ForeignKey(Fillials)
    image = models.ImageField(upload_to='fillials/gallery')

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=45)
    price = models.IntegerField()
    fillal = models.ForeignKey(Fillials)

    def __str__(self):
        return self.title
