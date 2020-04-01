# from datetime import datetime
#
# from django.db import models
#
#
# class UserProfile(models.Model):
#     """User table"""
#     id = models.AutoField(primary_key=True)  # although the django will create this one automatically
#     username = models.CharField(max_length=128, unique=True)
#     password = models.CharField(max_length=256)
#     email = models.EmailField(unique=True)
#     artist = models.BooleanField(default=True)
#     c_time = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=False)
#     # referee = models.CharField(max_length=256)
#     # realName = models.CharField(max_length=256)
#     refEmail = models.EmailField(unique=True)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         ordering = ['c_time']
#         verbose_name = 'user'
#         verbose_name_plural = 'users'