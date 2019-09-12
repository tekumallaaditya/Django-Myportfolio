from django.db import models

class introPageInfo(models.Model):
    first_intro = models.CharField(max_length=200)
    main_into = models.TextField()
    main_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return 'intro'