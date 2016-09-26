# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Shifts
from .forms import ShiftChangeForm
from .utils import current_year_week


def onduty_current_week(request):
    week = current_year_week()
    return HttpResponse(Shifts.onduty_person_name(week))

def onduty_next_week(request):
    week = current_year_week() + 1
    return HttpResponse(Shifts.onduty_person_name(week))

@login_required(login_url='/login/')
def reset(request):
    Shifts.assign()
    return HttpResponse("La asignación de guardias ha sido reseteada")

@login_required(login_url='/login/')
def shift_change(request):
    if request.method == 'POST':
        form = ShiftChangeForm(request.POST)
        if form.is_valid():
            Shifts.swap(form.cleaned_data.get('first_date'),
                        form.cleaned_data.get('second_date'))
            return HttpResponseRedirect('/')
    else:
        form = ShiftChangeForm()

    return render(request, 'shift_change_form.html', {'form': form})
