import datetime

def year_week(date):
    return date.isocalendar()[1]

def current_year_week():
    today = datetime.datetime.now().date()
    return year_week(today)

