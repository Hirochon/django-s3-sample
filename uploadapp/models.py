from django.db import models

from django.db import models

class PhotoModel(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.url
