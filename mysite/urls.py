"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

import main.views as main_views     # import views
import guestbook.views as guestbook_views
import user.views as user_views
import board.views as board_views

urlpatterns = [
    path('', main_views.index),

    path('user/joinform/', user_views.joinform),
    path('user/join', user_views.join), # POST 방식으로 보내려면 'user/joinsuccess' 맨 뒤에 / 붙이면 안된다.
    path('user/joinsuccess/', user_views.joinsuccess),
    path('user/loginform/', user_views.loginform),
    path('user/login', user_views.login),
    path('user/logout', user_views.logout),

    path('guestbook/', guestbook_views.index),
    path('guestbook/add', guestbook_views.add),
    path('guestbook/deleteform', guestbook_views.deleteform),
    path('guestbook/delete', guestbook_views.delete),

    path('board/', board_views.index),
    path('board/write', board_views.write),
    path('board/writeform', board_views.writeform),
    path('board/viewform', board_views.viewform),
    path('board/delete', board_views.delete),

    path('admin/', admin.site.urls)
]