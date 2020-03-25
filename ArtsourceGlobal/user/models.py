from django.db import models


class User(models.Model):
    """User table"""
    artist_choices = (
        ('Yes', True),
        ('No', False),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    artist = models.BooleanField(choices=artist_choices, default=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'users'
