from django.db import models


class workexp(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(default=None)
    start = models.DateField(default=None)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class education(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(default=None)
    start = models.DateField(default=None)
    end = models.DateField(default=None)

    def __str__(self):
        return self.title

class skills(models.Model):
    topic = models.CharField(max_length=200)
    def __str__(self):
        return self.topic

