# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.conf.urls import patterns, url

from apps.user.views import (login,
                             sign_up,
                             forgot,
                             logout,
                             itsi_login,
                             itsi_auth,
                             itsi_sign_up)

urlpatterns = patterns(
    '',
    url(r'^logout$', logout, name='logout'),
    url(r'^itsi/login$', itsi_login, name='itsi_login'),
    url(r'^itsi/authenticate$', itsi_auth, name='itsi_auth'),
    url(r'^itsi/sign_up', itsi_sign_up, name='itsi_sign_up'),
    url(r'^login$', login, name='login'),
    url(r'^sign_up$', sign_up, name='sign_up'),
    url(r'^forgot$', forgot, name='forgot')
)
