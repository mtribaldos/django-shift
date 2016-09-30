"""django_shifts URL Configuration
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('shifts.urls', namespace="shifts")),
]
