import datetime
from django.conf import settings


def year_week(date):
    anchor_date = settings.ANCHOR_DATE
    anchor_date_week_day = anchor_date.isocalendar()[2]
    days = (date - anchor_date).days
    return (days + anchor_date_week_day - 1) / 7

def current_year_week():
    today = datetime.datetime.now().date()
    return year_week(today)

