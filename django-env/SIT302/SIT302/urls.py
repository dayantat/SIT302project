"""SIT302 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include

urlpatterns = [
    path('admins/', admin.site.urls),  # In prod this line should be changed
    #  With the below anything that matches scrumboard/ will be looked for in the scrumboards/urls.py file
    re_path(r'^scrumboard/', include('scrumboard.urls'))  # include allows all extended urls to be imported from the file
]
