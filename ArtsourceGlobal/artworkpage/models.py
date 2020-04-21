from django.db import models
from user.models import User


# Create your models here.
class Artwork(models.Model):
    """Artwork table"""

    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='Img')
    thumbnail = models.ImageField(upload_to='Thumbnail')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'artwork'
        verbose_name_plural = 'artworks'

