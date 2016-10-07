# -*- encoding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShiftsAdminConfig(AppConfig):
    name = 'shifts'
    verbose_name = _("Shifts")
