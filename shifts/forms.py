
from django import forms
import datetime
#from functools import partial

#DateInput = partial(forms.DateInput, {'class': 'datepicker'})

from bootstrap_datepicker.widgets import DatePicker

class ShiftChangeForm(forms.Form):
    options = { "format": "dd/mm/yyyy",
                "autoclose": True,
                "weekStart": 1,
                "calendarWeeks": True,
                "daysOfWeekDisabled": [1,2,3,4,5],
                "startDate": '01/01/2016',
                "todayHighlight": True,
                "language": "es" }

    first_date = forms.DateField(
          widget=DatePicker(options = options))
    second_date = forms.DateField(
          widget=DatePicker(options = options))

