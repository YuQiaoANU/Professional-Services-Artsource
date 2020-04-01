from datetime import datetime

from django.db import models
from django_countries.fields import CountryField


class Interest(models.Model):
    # Painting, sculpture, photography, calligraphy, printmaking, arts and crafts, seal cutting, art design
    painting = models.BooleanField(default=True)
    sculpture = models.BooleanField(default=True)
    photography = models.BooleanField(default=True)
    calligraphy = models.BooleanField(default=True)
    printmaking = models.BooleanField(default=True)
    artsAndCrafts = models.BooleanField(default=True)
    sealCutting = models.BooleanField(default=True)
    artDesign = models.BooleanField(default=True)


class AdditionalInfo(models.Model):
    gender = models.CharField(max_length=8, blank=True)
    age = models.IntegerField(blank=True)
    street1 = models.CharField(max_length=512, blank=True)
    street2 = models.CharField(max_length=512, blank=True)
    suburb = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    postalCode = models.CharField(max_length=128, blank=True)
    country = CountryField(blank_label='Australia')
    phone = models.CharField(max_length=24, blank=True)


class User(models.Model):
    """User table"""
    # id = models.AutoField(primary_key=True)  # the django will create this one automatically
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    artist = models.BooleanField(default=False)
    c_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    # referee = models.CharField(max_length=256)
    # realName = models.CharField(max_length=256)
    refEmail = models.EmailField(unique=True, null=True)
    interest = models.OneToOneField(Interest, on_delete=models.CASCADE)
    additionalInfo = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']
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
