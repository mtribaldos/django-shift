"""django_shifts URL Configuration
"""
from django.contrib.auth.views import login, logout
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
#from shifts import views
from .views import ShiftsListView, onduty_current_week, onduty_next_week, onduty_previous_week, change_password, switch_shifts, reset

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='landing_page.html'), name="landing_page"),
    url(r'^current/', onduty_current_week, name="current_week"), 
    url(r'^today/', RedirectView.as_view(url='/current')),
    url(r'^next/', onduty_next_week, name="next_week"),
    url(r'^previous/', onduty_previous_week, name="previous_week"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^change-password', change_password, name="change_password"),
    url(r'^switch-shifts/', switch_shifts, name="switch_shifts"),
    url(r'^list-next-shifts/', ShiftsListView.as_view()),
    url(r'^reset/', reset, name="reset"),
]
