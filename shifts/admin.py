# -*- encoding: utf-8 -*-

import time
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Shifts


@admin.register(Shifts)
class ShiftsAdmin(admin.ModelAdmin):
    list_display = ['week_label', 'fullname']
    ordering = ('week',)

    def week_label(self, obj):
        return "Semana #%i" % obj.week

    def fullname(self, obj):
        return "%s" % obj.user.first_name
    fullname.short_description = _("Full name")


