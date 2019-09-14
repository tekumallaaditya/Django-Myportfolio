from django.db import models

class showresume(models.Model):
    res = models.FileField(upload_to='images/')
    def __str__(self):
        return 'Resume'