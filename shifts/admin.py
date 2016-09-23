# -*- encoding: utf-8 -*-

import time
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Shifts


class ShiftsAdmin(admin.ModelAdmin):
    list_display = ['week_label', 'fullname']
    ordering = ('week',)

    def week_label(self, obj):
        return "Semana #%i" % obj.week
        #return "Semana #%i (%s - %s)" % (obj.week, time.asctime(time.strptime('2016 %i 1' % obj.week, '%Y %W %w')), time.asctime(time.strptime('2016 %i 0' % obj.week, '%Y %W %w')))
        #return "Semana #%i (%s)" % (obj.week, time.strftime("%Y-%m-%d", time.strptime('2016 %i 1' % obj.week, '%Y %W %w')))

    def fullname(self, obj):
        return "%s" % obj.user.first_name
    fullname.short_description = _("Full name")

admin.site.register(Shifts, ShiftsAdmin)


