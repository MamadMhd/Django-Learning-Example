from django.urls import re_path
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    re_path(r'^others/$', views.other, name="Other"),
    re_path(r'^relative/$', views.relative, name="Relative"),
]
