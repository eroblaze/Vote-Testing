from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=30)
    vote = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

