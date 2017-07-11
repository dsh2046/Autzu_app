from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='nick_name', default='')
    birthday = models.DateField(verbose_name='birthday', null=True, blank=True)
    gender = models.CharField(choices=(('male', 'male'), ('female', 'female')), default='female', max_length=6)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='code')
    email = models.EmailField(max_length=50, verbose_name='email')
    send_type = models.CharField(choices=(('register', 'register'), ('forget', 'forget')), default='register', max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'EmailVerify'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.email


class License(models.Model):
    license_num = models.CharField(max_length=30, verbose_name='license_num')
    driver_name = models.CharField(max_length=100, verbose_name='driver_name')
    license_image = models.ImageField(upload_to="License_image/%Y/%m", default="license_image/default.png", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add_time')

    class Meta:
        verbose_name = 'License'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.driver_name


