import datetime

def current_year_week():
    week = datetime.datetime.now().date().isocalendar()[1]
    return week

