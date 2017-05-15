from django.db import models
from django.contrib.auth.models import User
from fillials.models import Fillials, FillialServices

# Create your models here.


class MasterType(models.Model):
    class Meta:
        verbose_name = 'Тип мастера'
        verbose_name_plural = 'Типы мастеров'
    title = models.CharField(max_length=45)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class MasterProfile(models.Model):
    class Meta:
        verbose_name = 'Профиль мастера'
        verbose_name_plural = 'Профили мастеров'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    master_type = models.ForeignKey(MasterType, null=True, default=None)
    fillial = models.ForeignKey(Fillials, null=True)
    image = models.ImageField(max_length=256, null=True, upload_to='profiles/')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=45, null=True)

    def __str__(self):
        return self.user.username


class MasterService(models.Model):
    class Meta:
        verbose_name = 'Услуги мастера'
        verbose_name_plural = 'Услуги мастеров'
    profile = models.ManyToManyField(MasterProfile, null=True, default=None)
    service = models.ForeignKey(FillialServices, default=None)
