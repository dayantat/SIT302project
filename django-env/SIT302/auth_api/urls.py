from django.urls import re_path

from .api import LoginView, LogoutView

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view()),
    re_path(r'^logout/$', LogoutView.as_view())
]