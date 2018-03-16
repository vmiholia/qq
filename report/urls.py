"""report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

VIEW ALL POSTS
The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel's content.

For the installation of the Django Debug Toolbar you need to have a django project where you can use pip in a Virtual Environment or without them. If you wan’t use pip, you can get the code of this component from here (https://github.com/jazzband/django-debug-toolbar) and put it in your django project path. But is more easy the pip installation and we will focus on this.

For installation we recommend use the virtual env and execute this command:

Bash
pip install django-debug-toolbar
The configuration of this component is simple, but because most of the configuration must be done in the core of the settings of the project, we recommend to do it independently.

First, in your general project urls.py, enter this code:

Python
"""

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('card.urls')),
]