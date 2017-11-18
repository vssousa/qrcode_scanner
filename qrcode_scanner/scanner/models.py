import datetime

from django.db import models

class QRCode(models.Model):
    message = models.CharField(max_length=500, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.message