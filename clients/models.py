from django.db import models
from fillials.models import Fillials 

# Create your models here.


class Clients(models.Model):
    # class Meta:
    name = models.CharField(max_length=45)
    fillial = models.ForeignKey(Fillials)

    def __str__(self):
        return self.name