"""django_shifts URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from shifts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^today/', views.onduty_today),
    url(r'^next_week/', views.onduty_next_week),
    url(r'^reset/', views.reset),
]
