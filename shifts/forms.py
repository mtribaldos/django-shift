
from django import forms
import datetime
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class ShiftChangeForm(forms.Form):
    first_date = forms.DateField(label='Primer turno', widget=DateInput())
    second_date = forms.DateField(label='Segundo turno', widget=DateInput())

