from django.db import models
from django.contrib.auth.models import User
# from pr

# Create your models here.


class Schedule(models.Model):
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    name = models.CharField("name", max_length=2000)
    date = models.DateField()
    time = models.CharField(max_length=45)
    master = models.ForeignKey(User)
