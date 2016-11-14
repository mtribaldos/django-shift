import time, datetime
from django.conf import settings


def year_week(date):
    anchor_date = settings.ANCHOR_DATE
    anchor_date_week_day = anchor_date.isocalendar()[2]
    days = (date - anchor_date).days
    return (days + anchor_date_week_day - 1) / 7

def current_year_week():
    today = datetime.datetime.now().date()
    return year_week(today)

def first_date_of_year_week(week):
    return settings.ANCHOR_DATE + datetime.timedelta(days=week*7) + datetime.timedelta(days=-(settings.ANCHOR_DATE.isocalendar()[2] - 1))
