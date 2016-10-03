# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Shifts
from .forms import ShiftChangeForm
from .utils import current_year_week



def onduty_current_week(request):
    week = current_year_week()
    return HttpResponse(Shifts.objects.onduty_person_name(week))


def onduty_next_week(request):
    week = current_year_week() + 1
    return HttpResponse(Shifts.objects.onduty_person_name(week))


def onduty_previous_week(request):
    week = current_year_week() - 1 
    return HttpResponse(Shifts.objects.onduty_person_name(week))


@login_required(login_url='/login/')
def reset(request):
    Shifts.objects.reset()
    return HttpResponse("La asignación de guardias ha sido reseteada")


@login_required(login_url='/login/')
def switch_shifts(request):
    if request.method == 'POST':
        form = ShiftChangeForm(request.POST)
        if form.is_valid():
            first_date, second_date = Shifts.objects.swap(form.cleaned_data.get('first_date'),
                                                          form.cleaned_data.get('second_date'))
            LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(first_date).pk,
                object_id       = first_date.week,
                object_repr     = 'switch_shifts',
                action_flag     = CHANGE,
                change_message  = "You have switched between week %i and %i" % (first_date.week, second_date.week))
            LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(second_date).pk,
                object_id       = second_date.week,
                object_repr     = 'switch_shifts',
                action_flag     = CHANGE,
                change_message  = "You have switched between week %i and %i" % (second_date.week, first_date.week))

            return redirect('shifts:landing_page')
    else:
        form = ShiftChangeForm()

    return render(request, 'switch_shifts_form.html', {'form': form})


@login_required(login_url='/login/')
def change_password(request):
    return HttpResponseRedirect('/admin/password_change/')    

