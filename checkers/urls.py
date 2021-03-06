"""checkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

import checkers_app.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#initial page presents user with the ability to login with existing username or create a new one
    url(r'^home/$', checkers_app.views.main),
    url(r'^check_login/$', checkers_app.views.check_login),
    url(r'^register/$', checkers_app.views.register),
    url(r'^getgames/$', checkers_app.views.getgames),
    url(r'^check_registration/$', checkers_app.views.check_registration),
    url(r'^new_game/$', checkers_app.views.new_game),
    url(r'^game/(?P<game_number>[0-9]+)$', checkers_app.views.game),
    url(r'^board/(?P<variable_square>[0-7]{2})$', checkers_app.views.board_click_square),
    url(r'^get_positions/(?P<game_number2>[0-9]+)$', checkers_app.views.get_positions),
]
