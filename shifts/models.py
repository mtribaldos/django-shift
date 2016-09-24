# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from django.db import models
from django.conf import settings


class StaffManager(models.Manager):
    def get_queryset(self):
        guard_group = Group.objects.filter(name = settings.SHIFT_GROUP_NAME)
        return super(StaffManager, self).get_queryset().filter(groups__in=guard_group)

@python_2_unicode_compatible
class Staff(User):
    objects = StaffManager()

    def __str__(self):
        return self.first_name

    class Meta:
        proxy = True


@python_2_unicode_compatible
class Shifts(models.Model):
    week = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Staff)

    def __str__(self):
        return str(self.week)

    @classmethod
    def assign(cls):
        staff = Staff.objects.all()
        count = staff.count()

        for i in range(1, 54):
            shift = cls(week=i, user=staff[i % count])
            shift.save()

    class Meta:
        verbose_name = _('shift')
        verbose_name_plural = _('shifts')
