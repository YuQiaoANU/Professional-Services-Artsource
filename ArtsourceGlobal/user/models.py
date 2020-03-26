from datetime import datetime

from django.db import models


class User(models.Model):
    """User table"""

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    artist = models.BooleanField(default=True)
    c_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'users'


class EmailVerifyRecord(models.Model):
    # verification code
    code = models.CharField(max_length=20, verbose_name="verifyCode")
    email = models.EmailField(max_length=50, verbose_name="email")
    # register verification and retrieve password when forget
    send_type = models.CharField(verbose_name="verifyCodeType", max_length=10,
                                 choices=(("register", "register"), ("forget", "retrieve")))
    send_time = models.DateTimeField(verbose_name="sendTime", default=datetime.now())

    class Meta:
        verbose_name = "Email verification code"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)