# -*- encoding: utf-8 -*-

from django.http import HttpResponse
import datetime
from .models import Shifts


def staff_today(request):
    week = datetime.datetime.now().date().isocalendar()[1]
    text = Shifts.objects.get(week=week)
    return HttpResponse(text.user.first_name)

def reset(request):
    Shifts.assign()
    return HttpResponse("La asignación de guardias ha sido reseteada")
