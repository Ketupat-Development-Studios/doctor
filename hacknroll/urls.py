from django.conf.urls import patterns, include, url
from django.contrib import admin
from hackapp.views import *

urlpatterns = patterns('',
    url(r'^ajax/login/$', login_view),
    url(r'^logout/$', logout_view),
    url(r'^ajax/get_markdown/(?P<url>\w+)/$', get_markdown),
    url(r'^ajax/edit_markdown/(?P<url>\w+)/$', edit_markdown),
    url(r'^ajax/delete_essay/(?P<url>\w+)/$', delete_essay),
    url(r'^ajax/create_essay/$', create_essay),
    url(r'^$', login_page),
    url(r'^main/$', main_page),
    url(r'^main/(?P<url>\w+)/$', main_essay),
    url(r'^admin/', include(admin.site.urls)),
)
