"""django_shifts URL Configuration
"""
from django.contrib.auth.views import login, logout
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from shifts import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='landing_page.html'), name="landing_page"),
    url(r'^current/', views.onduty_current_week, name="current_week"), 
    url(r'^today/', RedirectView.as_view(url='/current')),
    url(r'^next/', views.onduty_next_week, name="next_week"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^change-password', views.change_password, name="change_password"),
    url(r'^switch-shifts/', views.switch_shifts, name="switch_shifts"),
    url(r'^reset/', views.reset, name="reset"),
]
