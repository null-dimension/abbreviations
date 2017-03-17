"""abbreviations URL Configuration

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
from abbreviations.backends import MyRegistrationView
from django.conf.urls import url, include
from django.contrib import admin
from fullforms import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('fullforms.urls')),
    url(r'^$', views.index, name="fullforms"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name':'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done,
        {'template_name': 'registration/password_reset_done'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/add_fullform/$', views.addfullform,
        name='registration_add_fullform'),
    url(r'^accounts/profile/(?P<uname>[-\w@.+]+)/$', views.profile, name='user_profile'),
    url(r'^leaderboard/$', views.leaderboard, name='user_leaderboard'),
]
