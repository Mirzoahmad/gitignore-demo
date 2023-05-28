from django.db import models

# Create your models here.


class Cards(models.Model):
    title = models.CharField(verbose_name="name", max_length=30)
    cost = models.IntegerField(verbose_name='cost', blank=True, null=True)
    description = models.TextField(verbose_name='description')
    date_create = models.DateTimeField(verbose_name="created", auto_now_add=True)
    img_card = models.ImageField(verbose_name="image", blank=True) # blank=True eto znachit ne obyazatelno zapolnit polya

class Meta:
    verbose_name = "product"
    verbose_name_plural = "products"

    def __str__(self):
        return f'{self.title}'