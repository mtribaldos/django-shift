
from django import forms
import datetime
from bootstrap_datepicker.widgets import DatePicker


class ShiftChangeForm(forms.Form):
    options = { 
        "format": "dd/mm/yyyy",
        "autoclose": True,
        "weekStart": 1,
        "calendarWeeks": True,
        "daysOfWeekHighlighted": [5, 6, 0],
        "startDate": '01/01/2016',
        "endDate": '31/12/2030',
        "todayHighlight": True,
        "language": "es" }

    date_picker_widget = DatePicker(options=options)
    first_date = forms.DateField(widget=date_picker_widget, label='Primera fecha')
    second_date = forms.DateField(widget=date_picker_widget, label='Segunda fecha')
