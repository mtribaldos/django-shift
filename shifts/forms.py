
from django import forms
import datetime
from bootstrap_datepicker.widgets import DatePicker


class ShiftChangeForm(forms.Form):
    options = { 
        "format": "dd/mm/yyyy",
        "autoclose": True,
        "weekStart": 1,
        "calendarWeeks": True,
        "daysOfWeekHighlighted": [6, 0],
        "startDate": '01/01/2016',
        "todayHighlight": True,
        "language": "es" }

    first_date = forms.DateField(
        widget = DatePicker(options = options),
        label = 'Primera fecha')
    second_date = forms.DateField(
        widget = DatePicker(options = options),
        label = 'Segunda fecha')

