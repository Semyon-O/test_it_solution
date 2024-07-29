from django.db import models

# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    amount_of_watches = models.IntegerField()
    position = models.IntegerField()
