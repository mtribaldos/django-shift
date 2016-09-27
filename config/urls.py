"""django_shifts URL Configuration
"""
from django.contrib.auth.views import login
from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib import admin
from shifts import views

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^current_week/', views.onduty_current_week),
    url(r'^today/', RedirectView.as_view(url='/current_week')),
    url(r'^next_week/', views.onduty_next_week),
    url(r'^reset/', views.reset),
    url(r'^shift_change/', views.shift_change),
    url(r'^$', RedirectView.as_view(url='/current_week')),
]
