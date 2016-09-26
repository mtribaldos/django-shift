# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from .managers import StaffManager, ShiftsManager



@python_2_unicode_compatible
class Staff(User):
    objects = StaffManager()

    def __str__(self):
        return self.first_name

    class Meta:
        proxy = True


@python_2_unicode_compatible
class Shifts(models.Model):
    objects = ShiftsManager()

    week = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Staff)

    def __str__(self):
        return str(self.week)

    class Meta:
        #proxy = True
        verbose_name = _('shift')
        verbose_name_plural = _('shifts')
