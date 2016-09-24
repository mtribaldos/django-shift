# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from .models import Shifts
from .utils import current_year_week


def onduty_today(request):
    week = current_year_week()
    return HttpResponse(Shifts.onduty_person_name(week))

def onduty_next_week(request):
    week = current_year_week() + 1
    return HttpResponse(Shifts.onduty_person_name(week))

def reset(request):
    Shifts.assign()
    return HttpResponse("La asignación de guardias ha sido reseteada")
