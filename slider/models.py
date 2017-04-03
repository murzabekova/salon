from django.db import models


# Create your models here.


class Slider(models.Model):
    """docstring for Slider"""
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
    image = models.ImageField(upload_to='slider/images')
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
