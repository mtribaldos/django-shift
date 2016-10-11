# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings
from .utils import year_week


class StaffManager(models.Manager):
    def get_queryset(self):
        shifts_group = Group.objects.filter(name=settings.SHIFT_GROUP_NAME)
        return super(StaffManager, self).get_queryset().filter(groups__in=shifts_group)


class ShiftsManager(models.Manager):
    def onduty_person_name(self, week):
       onduty = self.get(week=week)
       return onduty.user.first_name

    def swap(self, first_date, second_date):
       onduty_first_date = self.get(week=year_week(first_date))
       onduty_second_date = self.get(week=year_week(second_date))
       onduty_first_date.user, onduty_second_date.user = onduty_second_date.user, onduty_first_date.user
       onduty_first_date.save()
       onduty_second_date.save()
       return onduty_first_date, onduty_second_date

    def reset(self):
        from .models import Staff 
        count = len(settings.SHIFT_USERS)

        for i in range(1, settings.SHIFT_CARDINALITY):
            user = Staff.objects.get(username=settings.SHIFT_USERS[i % count])
            shift, _ = self.update_or_create(week=i, defaults={'user': user})

